# Phishylix AI

AI-Driven Phishing Detection using Machine Learning and Explainable Browser-Based Analysis

---

## Overview

Phishylix AI is a machine-learning-based phishing detection system developed as part of an MSc Cyber Security research project at the University of Essex Online.

The project focuses on identifying AI-generated phishing webpages using engineered URL, HTML and textual webpage features. The artefact combines machine-learning experimentation, explainable phishing analysis and browser-based deployment to improve phishing-detection transparency and usability.

The system includes:

- Flask-based phishing analysis interface
- Chrome browser extension
- Explainability-oriented feature reporting
- Machine-learning phishing classification
- URL and HTML feature extraction
- Real-time webpage analysis

---

## Features

- Detects AI-generated phishing webpages
- Analyses webpage URL and HTML structure
- Provides phishing confidence scores
- Displays explainability-based feature reports
- Browser extension for real-time webpage scanning
- Flask-based interactive user interface
- Supervised machine-learning classification

---

## Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- BeautifulSoup
- Matplotlib
- HTML
- CSS
- JavaScript
- Chrome Extension APIs

---

## Project Structure

```text
Phishylix-AI/
│
├── ai_generated_phishing/
├── legitimate/
├── browser_extension/
├── models/
├── reports/
├── src/
├── app/
├── README.md
└── requirements.txt
```

---

## Machine-Learning Models

The project evaluates multiple supervised machine-learning models, including:

- Logistic Regression
- Random Forest
- Gradient Boosting

The final deployed model was selected based on:

- classification accuracy
- explainability
- computational efficiency
- browser integration suitability

---

## Installation and Running

Install required dependencies:

```bash
pip install -r requirements.txt
```

Train the phishing-detection model:

```bash
python src/train_model.py
```

Run the Flask web application:

```bash
python src/web_app.py
```

Open the application in a browser:

```text
http://127.0.0.1:5000
```

---

## Browser Extension

The project includes a Google Chrome browser extension capable of analysing webpages in real time using the trained phishing-detection model.

To load the extension:

1. Open Chrome Extensions
2. Enable Developer Mode
3. Select “Load unpacked”
4. Choose the `browser_extension` folder

---

## Evaluation

The artefact was evaluated using:

- Accuracy
- Macro F1-score
- ROC-AUC
- Confusion Matrix Analysis
- Real-world browser testing

---

## Ethical Disclaimer

This project was developed strictly for academic and defensive cybersecurity research purposes.

All phishing webpages used during experimentation were generated within controlled offline environments using synthetic or modified branding and non-functional interfaces. The artefact must not be used for malicious, deceptive or unauthorised activities.

The research was conducted in accordance with ethical cybersecurity experimentation principles and focused solely on phishing detection and defensive analysis.

---

## Author

Ketan Mone

MSc Cyber Security  
University of Essex Online

---

## Research Repository

GitHub Repository:

https://github.com/ketanmone/Phishylix-AI
