from pathlib import Path
import pandas as pd
from feature_extraction import extract_features, extract_text


LABELS = {
    "legitimate": 0,
    "ai_generated_phishing": 1
}


def build_dataset():
    rows = []

    for label_name, label_id in LABELS.items():
        folder = Path("data") / label_name

        for file in folder.glob("*.html"):
            html = file.read_text(encoding="utf-8", errors="ignore")

            if label_name == "legitimate":
                url = f"https://www.example-{file.stem}.com"
            else:
                url = f"https://demo-{file.stem}.login-verify.example"

            features = extract_features(url, html)
            features["text_content"] = extract_text(html)
            features["label"] = label_id
            features["file_name"] = file.name
            features["class_name"] = label_name

            rows.append(features)

    return pd.DataFrame(rows)