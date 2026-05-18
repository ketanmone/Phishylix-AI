from urllib.parse import urlparse
from bs4 import BeautifulSoup, MarkupResemblesLocatorWarning
import math
import re
import warnings

warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)


def calculate_entropy(text):
    if not text:
        return 0

    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    entropy = 0
    for count in frequency.values():
        probability = count / len(text)
        entropy -= probability * math.log2(probability)

    return entropy


def extract_visible_text(html):
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    return soup.get_text(" ", strip=True).lower()


def extract_features(url, html):
    soup = BeautifulSoup(html, "html.parser")
    text = extract_visible_text(html)

    parsed_url = urlparse(url)
    domain = parsed_url.netloc.lower()
    path = parsed_url.path.lower()

    trusted_domains = [
        "hdfc.bank.in",
        "icici.bank.in",
        "sbi.co.in",
        "axisbank.com",
        "incometax.gov.in",
        "uidai.gov.in",
        "india.gov.in",
        "amazon.in",
        "flipkart.com",
        "airtel.in",
        "jio.com",
        "licindia.in"
    ]

    suspicious_text_phrases = [
        "urgent",
        "verify immediately",
        "account suspended",
        "temporarily suspended",
        "restore access",
        "failure to verify",
        "within 24 hours",
        "account deletion",
        "unusual activity detected",
        "otp confirmation",
        "verify your account"
    ]

    suspicious_url_words = [
        "verify",
        "restore",
        "validate",
        "confirm",
        "suspend",
        "password-reset",
        "login-verify"
    ]

    features = {
        "url_length": len(url),
        "url_entropy": calculate_entropy(url),
        "num_dots": url.count("."),
        "num_hyphens": url.count("-"),
        "num_digits": sum(c.isdigit() for c in url),
        "num_slashes": url.count("/"),
        "num_query_params": url.count("&") + url.count("?"),
        "has_https": int(parsed_url.scheme == "https"),
        "has_ip_pattern": int(bool(re.search(r"(?:\d{1,3}\.){3}\d{1,3}", url))),

        "domain_length": len(domain),
        "is_known_trusted_domain": int(any(td in domain for td in trusted_domains)),
        "is_bank_in_domain": int(domain.endswith("bank.in")),
        "is_gov_in_domain": int(domain.endswith("gov.in")),
        "is_nic_in_domain": int(domain.endswith("nic.in")),
        "trusted_domain_strength": sum(1 for td in trusted_domains if td in domain),

        "has_login_word_url": int("login" in url.lower()),
        "has_verify_word_url": int("verify" in url.lower()),
        "has_secure_word_url": int("secure" in url.lower()),
        "suspicious_url_word_count": sum(
            domain.count(word) + path.count(word)
            for word in suspicious_url_words
        ),

        "num_forms": min(len(soup.find_all("form")), 10),
        "num_inputs": min(len(soup.find_all("input")), 20),
        "num_password_inputs": min(len(soup.find_all("input", {"type": "password"})), 5),
        "num_email_inputs": min(len(soup.find_all("input", {"type": "email"})), 5),
        "num_links": min(len(soup.find_all("a")), 100),
        "num_scripts": min(len(soup.find_all("script")), 20),
        "num_buttons": min(len(soup.find_all("button")), 20),
        "num_images": min(len(soup.find_all("img")), 50),

        "html_length": min(len(html), 50000),
        "text_length": min(len(text), 20000),
        "word_count": min(len(text.split()), 3000),
        "has_demo_watermark": int("demo only" in text),

        "suspicious_word_count": sum(
            text.count(phrase)
            for phrase in suspicious_text_phrases
        ),

        "legitimate_service_word_count": sum(
            text.count(word)
            for word in [
                "privacy",
                "terms",
                "contact us",
                "about us",
                "customer service",
                "support",
                "branches",
                "careers",
                "investor",
                "products",
                "services"
            ]
        )
    }

    return features


def extract_text(html):
    return extract_visible_text(html)