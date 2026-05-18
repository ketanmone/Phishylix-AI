import argparse
import joblib
import pandas as pd
from pathlib import Path
from feature_extraction import extract_features


LABELS = {
    0: "legitimate",
    1: "traditional_phishing",
    2: "ai_generated_phishing"
}


parser = argparse.ArgumentParser()
parser.add_argument("--url", required=True)
parser.add_argument("--html", required=True)
args = parser.parse_args()

html = Path(args.html).read_text(encoding="utf-8", errors="ignore")
features = extract_features(args.url, html)

model = joblib.load("models/phishing_detector.pkl")
prediction = model.predict(pd.DataFrame([features]))[0]

print("Prediction:", LABELS[prediction])