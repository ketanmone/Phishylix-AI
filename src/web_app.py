from flask import Flask, render_template, request
import joblib
import pandas as pd
import requests

from feature_extraction import extract_features, extract_text


app = Flask(
    __name__,
    template_folder="../app/templates",
    static_folder="../app/static",
    static_url_path="/static"
)

model_bundle = joblib.load("models/phishing_detector.pkl")
model = model_bundle["model"]
numeric_columns = model_bundle["numeric_columns"]
label_names = model_bundle["label_names"]


def generate_feature_report(features):
    report = []
    explain_score = 0

    descriptions = {
        "url_length": "Length of the website URL",
        "url_entropy": "Randomness or complexity of the URL",
        "num_dots": "Number of dots in the URL",
        "num_hyphens": "Number of hyphens in the URL",
        "num_digits": "Number of digits in the URL",
        "num_slashes": "Number of slashes in the URL",
        "num_query_params": "Number of query parameters in the URL",
        "has_https": "Checks whether HTTPS is used",
        "has_ip_pattern": "Checks whether URL uses an IP address",
        "has_login_word_url": "Checks if URL contains login",
        "has_verify_word_url": "Checks if URL contains verify",
        "has_secure_word_url": "Checks if URL contains secure",
        "has_update_word_url": "Checks if URL contains update",
        "domain_length": "Length of the domain name",
        "is_known_trusted_domain": "Checks whether domain matches known trusted organisations",
        "is_bank_in_domain": "Checks whether domain uses bank.in pattern",
        "is_gov_in_domain": "Checks whether domain uses gov.in pattern",
        "is_nic_in_domain": "Checks whether domain uses nic.in pattern",
        "is_co_in_domain": "Checks whether domain uses co.in pattern",
        "trusted_domain_strength": "Strength of trusted-domain match",
        "suspicious_domain_word_count": "Suspicious words found in domain or path",
        "num_forms": "Number of forms on the page",
        "num_inputs": "Number of input fields",
        "num_password_inputs": "Number of password fields",
        "num_email_inputs": "Number of email fields",
        "num_links": "Number of hyperlinks",
        "num_scripts": "Number of scripts",
        "num_buttons": "Number of buttons",
        "num_images": "Number of images",
        "html_length": "Overall HTML size",
        "text_length": "Visible text length",
        "word_count": "Total visible word count",
        "has_demo_watermark": "Checks demo-only watermark",
        "suspicious_word_count": "Count of suspicious or urgency-based words",
        "legitimate_service_word_count": "Count of normal service-related words"
    }

    for key, value in features.items():
        risk = "Low"

        if key in [
            "num_query_params",
            "has_ip_pattern",
            "num_password_inputs",
            "suspicious_word_count",
            "suspicious_domain_word_count"
        ]:
            if value >= 3:
                risk = "High"
                explain_score += 6
            elif value >= 1:
                risk = "Medium"
                explain_score += 3

        elif key in ["num_forms", "num_inputs", "num_email_inputs"]:
            if value > 5:
                risk = "High"
                explain_score += 4
            elif value >= 1:
                risk = "Medium"
                explain_score += 2

        elif key in ["url_length", "url_entropy"]:
            if value > 100:
                risk = "High"
                explain_score += 4
            elif value > 40:
                risk = "Medium"
                explain_score += 2

        elif key in ["is_known_trusted_domain", "trusted_domain_strength", "is_gov_in_domain", "is_bank_in_domain"]:
            if value >= 1:
                risk = "Low"
                explain_score -= 5

        elif key == "has_demo_watermark" and value == 1:
            risk = "High"
            explain_score += 5

        report.append({
            "feature": key,
            "description": descriptions.get(key, "Extracted webpage feature"),
            "value": value,
            "risk": risk
        })

    explain_score = max(explain_score, 0)

    if explain_score <= 5:
        explain_label = "Low explainability risk"
    elif explain_score <= 15:
        explain_label = "Moderate explainability risk"
    else:
        explain_label = "High explainability risk"

    return report, explain_score, explain_label


def analyse_page(url, html):
    features = extract_features(url, html)
    text_content = extract_text(html)

    input_data = pd.DataFrame([features])
    input_data["text_content"] = text_content
    input_data = input_data[numeric_columns + ["text_content"]]

    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]

    result = label_names[prediction]
    confidence = round(float(max(probabilities)) * 100, 2)

    feature_report, explain_score, explain_label = generate_feature_report(features)

    if result == "legitimate":
        risk_level = "Low Risk"
        alert_message = "This website appears legitimate based on the current model analysis."
    else:
        risk_level = "High Risk"
        alert_message = "This website shows patterns similar to AI-generated phishing pages."

    return {
        "result": result,
        "confidence": confidence,
        "risk_level": risk_level,
        "alert_message": alert_message,
        "feature_report": feature_report,
        "explain_score": explain_score,
        "explain_label": explain_label
    }


@app.route("/api/analyse", methods=["POST"])
def api_analyse():
    try:
        data = request.get_json()
        url = data.get("url", "")
        html = data.get("html", "")

        analysis = analyse_page(url, html)

        return {
            "result": analysis["result"],
            "confidence": analysis["confidence"],
            "risk_level": analysis["risk_level"],
            "alert_message": analysis["alert_message"],
            "explain_score": analysis["explain_score"],
            "explain_label": analysis["explain_label"],
            "feature_report": analysis["feature_report"]
        }

    except Exception as e:
        return {"error": str(e)}, 500


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    confidence = None
    risk_level = None
    alert_message = None
    error = None
    tested_url = None
    feature_report = None
    explain_score = None
    explain_label = None

    if request.method == "POST":
        url = request.form.get("url", "").strip()
        uploaded_file = request.files.get("html_file")

        try:
            if uploaded_file and uploaded_file.filename.endswith(".html"):
                html = uploaded_file.read().decode("utf-8", errors="ignore")
                tested_url = uploaded_file.filename
                url_for_features = f"http://secure-{uploaded_file.filename}.login-verify.net"

            elif url:
                response = requests.get(url, timeout=10)
                html = response.text
                tested_url = url
                url_for_features = url

            else:
                error = "Please enter a website URL or upload an HTML file."
                return render_template(
                    "index.html",
                    result=result,
                    confidence=confidence,
                    risk_level=risk_level,
                    alert_message=alert_message,
                    error=error,
                    tested_url=tested_url,
                    feature_report=feature_report,
                    explain_score=explain_score,
                    explain_label=explain_label
                )

            analysis = analyse_page(url_for_features, html)

            result = analysis["result"]
            confidence = analysis["confidence"]
            risk_level = analysis["risk_level"]
            alert_message = analysis["alert_message"]
            feature_report = analysis["feature_report"]
            explain_score = analysis["explain_score"]
            explain_label = analysis["explain_label"]

        except Exception as e:
            error = f"Could not analyse the website. Reason: {str(e)}"

    return render_template(
        "index.html",
        result=result,
        confidence=confidence,
        risk_level=risk_level,
        alert_message=alert_message,
        error=error,
        tested_url=tested_url,
        feature_report=feature_report,
        explain_score=explain_score,
        explain_label=explain_label
    )


app.run(debug=True)