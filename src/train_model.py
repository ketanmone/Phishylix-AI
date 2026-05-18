from pathlib import Path
import json
import joblib
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
    f1_score,
    roc_auc_score
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from dataset_loader import build_dataset


Path("models").mkdir(exist_ok=True)
Path("reports/figures").mkdir(parents=True, exist_ok=True)

df = build_dataset()

label_names = [
    "legitimate",
    "ai_generated_phishing"
]

print("\nDataset class distribution:")
print(df["class_name"].value_counts())

if df["label"].nunique() < 2:
    raise ValueError(
        "Training requires both classes: legitimate and ai_generated_phishing."
    )

if df["label"].value_counts().min() < 2:
    raise ValueError(
        "Each class must have at least 2 HTML files. Add more files to both folders."
    )

metadata_columns = ["label", "file_name", "class_name"]
numeric_columns = [
    col for col in df.columns
    if col not in metadata_columns + ["text_content"]
]

X = df[numeric_columns + ["text_content"]]
y = df["label"]

X_train, X_test, y_train, y_test, train_files, test_files = train_test_split(
    X,
    y,
    df[["file_name", "class_name"]],
    test_size=0.25,
    random_state=42,
    stratify=y
)

preprocessor = ColumnTransformer(
    transformers=[
        ("numeric", StandardScaler(), numeric_columns),
        ("text", TfidfVectorizer(max_features=150), "text_content")
    ]
)

models = {
    "Logistic Regression": Pipeline([
        ("preprocessor", preprocessor),
        ("model", LogisticRegression(max_iter=1000, class_weight="balanced"))
    ]),
    "Random Forest": Pipeline([
        ("preprocessor", preprocessor),
        ("model", RandomForestClassifier(
            n_estimators=200,
            random_state=42,
            class_weight="balanced"
        ))
    ]),
    "Gradient Boosting": Pipeline([
        ("preprocessor", preprocessor),
        ("model", GradientBoostingClassifier(random_state=42))
    ])
}

results = {}
best_model = None
best_model_name = ""
best_f1 = -1

for name, model in models.items():
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(X_test)
        positive_class_probability = probabilities[:, 1]
    else:
        probabilities = None
        positive_class_probability = None

    accuracy = accuracy_score(y_test, predictions)
    macro_f1 = f1_score(y_test, predictions, average="macro", zero_division=0)

    try:
        roc_auc = roc_auc_score(y_test, positive_class_probability)
    except Exception:
        roc_auc = None

    results[name] = {
        "accuracy": round(float(accuracy), 4),
        "macro_f1": round(float(macro_f1), 4),
        "roc_auc": round(float(roc_auc), 4) if roc_auc is not None else None,
        "classification_report": classification_report(
            y_test,
            predictions,
            labels=[0, 1],
            target_names=label_names,
            output_dict=True,
            zero_division=0
        )
    }

    print("\n", name)
    print("Accuracy:", accuracy)
    print("Macro F1:", macro_f1)
    print("ROC-AUC:", roc_auc)

    if macro_f1 > best_f1:
        best_f1 = macro_f1
        best_model = model
        best_model_name = name

joblib.dump(
    {
        "model": best_model,
        "numeric_columns": numeric_columns,
        "label_names": label_names
    },
    "models/phishing_detector.pkl"
)

best_predictions = best_model.predict(X_test)
best_probabilities = best_model.predict_proba(X_test)

print("\nBest Model:", best_model_name)
print("\nClassification Report:")
print(classification_report(
    y_test,
    best_predictions,
    labels=[0, 1],
    target_names=label_names,
    zero_division=0
))

metrics = {
    "dataset_size": int(len(df)),
    "train_size": int(len(X_train)),
    "test_size": int(len(X_test)),
    "class_distribution": df["class_name"].value_counts().to_dict(),
    "best_model": best_model_name,
    "results": results,
    "numeric_columns": numeric_columns
}

with open("reports/metrics.json", "w", encoding="utf-8") as file:
    json.dump(metrics, file, indent=4)

cm = confusion_matrix(y_test, best_predictions, labels=[0, 1])

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["legitimate", "ai_phishing"]
)

disp.plot()
plt.title(f"Confusion Matrix - {best_model_name}")
plt.tight_layout()
plt.savefig("reports/figures/confusion_matrix.png")
plt.close()

comparison_df = pd.DataFrame([
    {
        "Model": model_name,
        "Accuracy": model_results["accuracy"],
        "Macro F1": model_results["macro_f1"],
        "ROC-AUC": model_results["roc_auc"] if model_results["roc_auc"] is not None else 0
    }
    for model_name, model_results in results.items()
])

comparison_df.plot(
    x="Model",
    y=["Accuracy", "Macro F1", "ROC-AUC"],
    kind="bar"
)

plt.title("Model Performance Comparison")
plt.ylabel("Score")
plt.ylim(0, 1.05)
plt.xticks(rotation=20, ha="right")
plt.tight_layout()
plt.savefig("reports/figures/model_comparison.png")
plt.close()

error_rows = []

y_test_list = list(y_test)

for index, actual in enumerate(y_test_list):
    predicted = int(best_predictions[index])

    if actual != predicted:
        error_rows.append({
            "file_name": test_files.iloc[index]["file_name"],
            "actual_class": label_names[int(actual)],
            "predicted_class": label_names[predicted],
            "confidence": round(float(max(best_probabilities[index])) * 100, 2)
        })

error_df = pd.DataFrame(error_rows)

if error_df.empty:
    error_df = pd.DataFrame([{
        "file_name": "No misclassifications",
        "actual_class": "-",
        "predicted_class": "-",
        "confidence": "-"
    }])

error_df.to_csv("reports/error_analysis.csv", index=False)

print("\nModel saved at: models/phishing_detector.pkl")
print("Metrics saved at: reports/metrics.json")
print("Confusion matrix saved at: reports/figures/confusion_matrix.png")
print("Model comparison graph saved at: reports/figures/model_comparison.png")
print("Error analysis saved at: reports/error_analysis.csv")