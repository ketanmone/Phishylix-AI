from pathlib import Path
import random


BASE_DIR = Path("data")

FOLDERS = [
    BASE_DIR / "legitimate",
    BASE_DIR / "traditional_phishing",
    BASE_DIR / "ai_generated_phishing"
]

for folder in FOLDERS:
    folder.mkdir(parents=True, exist_ok=True)


indian_legitimate_brands = [
    "BharatTrust Bank",
    "Sahyadri Finance",
    "Nivaas Home Loans",
    "UrbanHaul India",
    "DesiCart",
    "BazaarOne",
    "ConnectBharat Telecom",
    "MetroFiber India",
    "SurakshaCover Insurance",
    "JeevanSure Health",
    "YatraVista Travel",
    "RailEase Services",
    "CampusSetu University",
    "MediSutra Clinic",
    "GramPay Digital"
]


traditional_phishing_brands = [
    "Secure Account Desk",
    "India Verification Portal",
    "Customer Safety Centre",
    "Account Restore Team",
    "Payment Validation Desk",
    "Digital KYC Update",
    "Online Access Recovery",
    "Security Alert Centre",
    "User Protection Desk",
    "Login Verification Hub"
]


ai_generated_brands = [
    "AaravPay",
    "NivaasSecure",
    "SutraBank",
    "UrbanSetu",
    "IndigoLedger",
    "Vyoma Finance",
    "Pragati Wallet",
    "SaffronCart",
    "Triveni Loans",
    "SurakshaOne"
]


legitimate_template = """
<!DOCTYPE html>
<html>
<head>
<title>{brand} - Official Customer Information</title>
<style>
body {{
    font-family: Arial, sans-serif;
    margin: 0;
    background: #f5f7fb;
    color: #1f2937;
}}
header {{
    background: #17324d;
    color: white;
    padding: 28px;
}}
main {{
    max-width: 900px;
    margin: 35px auto;
    background: white;
    padding: 32px;
    border-radius: 18px;
}}
.section {{
    border: 1px solid #e5e7eb;
    padding: 20px;
    border-radius: 14px;
    margin-top: 18px;
}}
a {{
    color: #17324d;
}}
.notice {{
    margin-top: 25px;
    font-size: 13px;
    color: #6b7280;
}}
</style>
</head>
<body>
<header>
<h1>{brand}</h1>
<p>Fictional Indian customer information webpage</p>
</header>

<main>
<h2>Welcome to {brand}</h2>
<p>
{brand} provides customer support, product information and digital service guidance
for users across India. This static page is created for academic machine-learning
testing only.
</p>

<div class="section">
<h3>Services</h3>
<p>{service_text}</p>
<a href="#">View information</a>
</div>

<div class="section">
<h3>Customer Support</h3>
<p>Users can read FAQs, understand services and access general help information.</p>
</div>

<p class="notice">DEMO ONLY - Fictional legitimate-style webpage. No real organisation. No credential collection.</p>
</main>
</body>
</html>
"""


traditional_template = """
<!DOCTYPE html>
<html>
<head>
<title>Immediate Account Verification Required</title>
<style>
body {{
    font-family: Verdana, sans-serif;
    background: #ffffff;
    color: #222222;
}}
.container {{
    max-width: 650px;
    margin: 45px auto;
    padding: 24px;
    border: 1px solid #cccccc;
}}
.warning {{
    color: #b00020;
    font-weight: bold;
}}
input {{
    width: 95%;
    padding: 10px;
    margin: 8px 0;
}}
button {{
    background: #b00020;
    color: white;
    padding: 12px 18px;
    border: none;
}}
.demo {{
    margin-top: 20px;
    color: #777777;
    font-size: 12px;
}}
</style>
</head>
<body>
<div class="container">
<h1>{brand}</h1>
<p class="warning">{warning_text}</p>
<p>
Your account access may be limited. Please verify your details immediately
to restore full online services.
</p>

<form onsubmit="return false;">
<label>Email or mobile number</label><br>
<input type="email" disabled placeholder="Disabled demo field"><br>

<label>Password</label><br>
<input type="password" disabled placeholder="Disabled demo field"><br>

<button type="button" disabled>Verify Account</button>
</form>

<p class="demo">DEMO ONLY - Fictional traditional phishing-style webpage. Form disabled. No credential collection.</p>
</div>
</body>
</html>
"""


ai_generated_template = """
<!DOCTYPE html>
<html>
<head>
<title>{brand} Secure Digital Access</title>
<style>
body {{
    margin: 0;
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #eef4ff, #ffffff);
    color: #172033;
}}
.wrapper {{
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 32px;
}}
.panel {{
    width: 920px;
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    background: white;
    border-radius: 28px;
    overflow: hidden;
    box-shadow: 0 24px 70px rgba(23, 32, 51, 0.12);
}}
.left {{
    padding: 48px;
    background: #13233f;
    color: white;
}}
.right {{
    padding: 48px;
}}
.badge {{
    display: inline-block;
    padding: 8px 12px;
    border-radius: 999px;
    background: rgba(255,255,255,0.14);
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.12em;
}}
h1 {{
    font-size: 40px;
    margin: 20px 0 14px;
}}
p {{
    line-height: 1.65;
}}
input {{
    width: 100%;
    padding: 14px;
    margin: 8px 0 16px;
    border: 1px solid #d8e0ec;
    border-radius: 14px;
}}
button {{
    width: 100%;
    padding: 15px;
    border: none;
    border-radius: 14px;
    background: #13233f;
    color: white;
    font-weight: bold;
}}
.demo {{
    margin-top: 18px;
    padding: 12px;
    border-radius: 12px;
    background: #fff7dd;
    color: #6b4e00;
    font-size: 13px;
}}
</style>
</head>
<body>
<div class="wrapper">
<section class="panel">
<div class="left">
<span class="badge">Fictional India digital portal</span>
<h1>{brand}</h1>
<p>{headline}</p>
<p>{description}</p>
</div>

<div class="right">
<h2>Secure Sign In</h2>
<p>Access your personalised dashboard and manage your service preferences.</p>

<form onsubmit="return false;">
<label>Email address or mobile number</label>
<input type="email" disabled placeholder="demo.user@example.com">

<label>Password</label>
<input type="password" disabled placeholder="Disabled for safety">

<button type="button" disabled>Continue Securely</button>
</form>

<div class="demo">
DEMO ONLY - Fictional AI-generated phishing-style page. Disabled form. No real brand. No credential capture.
</div>
</div>
</section>
</div>
</body>
</html>
"""


services = [
    "Digital banking, loan guidance and customer service information.",
    "Online shopping support, delivery guidance and order information.",
    "Telecom plan information, broadband services and help articles.",
    "Insurance policy guidance, claims information and customer support.",
    "Travel booking information, itinerary support and service updates.",
    "Healthcare appointment guidance and patient information services.",
    "Education services, student helpdesk and academic information.",
    "Digital wallet information, transaction guidance and safety awareness."
]

warnings = [
    "Urgent: your online access will be suspended.",
    "Immediate verification required to continue service.",
    "Your digital account has been temporarily restricted.",
    "Security update required for your customer profile.",
    "Limited access detected. Verify your account now.",
    "Your payment profile requires immediate confirmation."
]

headlines = [
    "A smarter and safer way to manage your digital services across India.",
    "Review your account preferences, service updates and protection settings.",
    "Experience seamless access to your personalised financial dashboard.",
    "Manage your digital identity, security preferences and support requests.",
    "A modern customer portal designed for secure online convenience."
]

descriptions = [
    "This fictional page uses polished language and modern layout patterns to represent AI-generated web content for research purposes.",
    "The design includes realistic content structure, dashboard-style messaging and security-focused microcopy for classification testing.",
    "This static webpage helps evaluate whether machine-learning models can distinguish polished synthetic pages from other webpage classes.",
    "The page is fully offline, non-functional and created only as a safe academic artefact for phishing-detection research."
]


# Remove old generated files only if they follow our naming pattern
for folder in FOLDERS:
    for file in folder.glob("*.html"):
        file.unlink()


for i in range(1, 51):
    brand = indian_legitimate_brands[(i - 1) % len(indian_legitimate_brands)]
    html = legitimate_template.format(
        brand=f"{brand} {i}",
        service_text=random.choice(services)
    )
    file_path = BASE_DIR / "legitimate" / f"legitimate_{i:03d}.html"
    file_path.write_text(html, encoding="utf-8")


for i in range(1, 51):
    brand = traditional_phishing_brands[(i - 1) % len(traditional_phishing_brands)]
    html = traditional_template.format(
        brand=f"{brand} {i}",
        warning_text=random.choice(warnings)
    )
    file_path = BASE_DIR / "traditional_phishing" / f"traditional_{i:03d}.html"
    file_path.write_text(html, encoding="utf-8")


for i in range(1, 51):
    brand = ai_generated_brands[(i - 1) % len(ai_generated_brands)]
    html = ai_generated_template.format(
        brand=f"{brand} {i}",
        headline=random.choice(headlines),
        description=random.choice(descriptions)
    )
    file_path = BASE_DIR / "ai_generated_phishing" / f"ai_generated_{i:03d}.html"
    file_path.write_text(html, encoding="utf-8")


print("150 dummy Indian-context HTML webpages created successfully.")
print("50 legitimate pages")
print("50 traditional phishing-style pages")
print("50 AI-generated phishing-style pages")
import random


BASE_DIR = Path("data")

FOLDERS = [
    BASE_DIR / "legitimate",
    BASE_DIR / "traditional_phishing",
    BASE_DIR / "ai_generated_phishing"
]

for folder in FOLDERS:
    folder.mkdir(parents=True, exist_ok=True)


indian_legitimate_brands = [
    "BharatTrust Bank",
    "Sahyadri Finance",
    "Nivaas Home Loans",
    "UrbanHaul India",
    "DesiCart",
    "BazaarOne",
    "ConnectBharat Telecom",
    "MetroFiber India",
    "SurakshaCover Insurance",
    "JeevanSure Health",
    "YatraVista Travel",
    "RailEase Services",
    "CampusSetu University",
    "MediSutra Clinic",
    "GramPay Digital"
]


traditional_phishing_brands = [
    "Secure Account Desk",
    "India Verification Portal",
    "Customer Safety Centre",
    "Account Restore Team",
    "Payment Validation Desk",
    "Digital KYC Update",
    "Online Access Recovery",
    "Security Alert Centre",
    "User Protection Desk",
    "Login Verification Hub"
]


ai_generated_brands = [
    "AaravPay",
    "NivaasSecure",
    "SutraBank",
    "UrbanSetu",
    "IndigoLedger",
    "Vyoma Finance",
    "Pragati Wallet",
    "SaffronCart",
    "Triveni Loans",
    "SurakshaOne"
]


legitimate_template = """
<!DOCTYPE html>
<html>
<head>
<title>{brand} - Official Customer Information</title>
<style>
body {{
    font-family: Arial, sans-serif;
    margin: 0;
    background: #f5f7fb;
    color: #1f2937;
}}
header {{
    background: #17324d;
    color: white;
    padding: 28px;
}}
main {{
    max-width: 900px;
    margin: 35px auto;
    background: white;
    padding: 32px;
    border-radius: 18px;
}}
.section {{
    border: 1px solid #e5e7eb;
    padding: 20px;
    border-radius: 14px;
    margin-top: 18px;
}}
a {{
    color: #17324d;
}}
.notice {{
    margin-top: 25px;
    font-size: 13px;
    color: #6b7280;
}}
</style>
</head>
<body>
<header>
<h1>{brand}</h1>
<p>Fictional Indian customer information webpage</p>
</header>

<main>
<h2>Welcome to {brand}</h2>
<p>
{brand} provides customer support, product information and digital service guidance
for users across India. This static page is created for academic machine-learning
testing only.
</p>

<div class="section">
<h3>Services</h3>
<p>{service_text}</p>
<a href="#">View information</a>
</div>

<div class="section">
<h3>Customer Support</h3>
<p>Users can read FAQs, understand services and access general help information.</p>
</div>

<p class="notice">DEMO ONLY - Fictional legitimate-style webpage. No real organisation. No credential collection.</p>
</main>
</body>
</html>
"""


traditional_template = """
<!DOCTYPE html>
<html>
<head>
<title>Immediate Account Verification Required</title>
<style>
body {{
    font-family: Verdana, sans-serif;
    background: #ffffff;
    color: #222222;
}}
.container {{
    max-width: 650px;
    margin: 45px auto;
    padding: 24px;
    border: 1px solid #cccccc;
}}
.warning {{
    color: #b00020;
    font-weight: bold;
}}
input {{
    width: 95%;
    padding: 10px;
    margin: 8px 0;
}}
button {{
    background: #b00020;
    color: white;
    padding: 12px 18px;
    border: none;
}}
.demo {{
    margin-top: 20px;
    color: #777777;
    font-size: 12px;
}}
</style>
</head>
<body>
<div class="container">
<h1>{brand}</h1>
<p class="warning">{warning_text}</p>
<p>
Your account access may be limited. Please verify your details immediately
to restore full online services.
</p>

<form onsubmit="return false;">
<label>Email or mobile number</label><br>
<input type="email" disabled placeholder="Disabled demo field"><br>

<label>Password</label><br>
<input type="password" disabled placeholder="Disabled demo field"><br>

<button type="button" disabled>Verify Account</button>
</form>

<p class="demo">DEMO ONLY - Fictional traditional phishing-style webpage. Form disabled. No credential collection.</p>
</div>
</body>
</html>
"""


ai_generated_template = """
<!DOCTYPE html>
<html>
<head>
<title>{brand} Secure Digital Access</title>
<style>
body {{
    margin: 0;
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #eef4ff, #ffffff);
    color: #172033;
}}
.wrapper {{
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 32px;
}}
.panel {{
    width: 920px;
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    background: white;
    border-radius: 28px;
    overflow: hidden;
    box-shadow: 0 24px 70px rgba(23, 32, 51, 0.12);
}}
.left {{
    padding: 48px;
    background: #13233f;
    color: white;
}}
.right {{
    padding: 48px;
}}
.badge {{
    display: inline-block;
    padding: 8px 12px;
    border-radius: 999px;
    background: rgba(255,255,255,0.14);
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.12em;
}}
h1 {{
    font-size: 40px;
    margin: 20px 0 14px;
}}
p {{
    line-height: 1.65;
}}
input {{
    width: 100%;
    padding: 14px;
    margin: 8px 0 16px;
    border: 1px solid #d8e0ec;
    border-radius: 14px;
}}
button {{
    width: 100%;
    padding: 15px;
    border: none;
    border-radius: 14px;
    background: #13233f;
    color: white;
    font-weight: bold;
}}
.demo {{
    margin-top: 18px;
    padding: 12px;
    border-radius: 12px;
    background: #fff7dd;
    color: #6b4e00;
    font-size: 13px;
}}
</style>
</head>
<body>
<div class="wrapper">
<section class="panel">
<div class="left">
<span class="badge">Fictional India digital portal</span>
<h1>{brand}</h1>
<p>{headline}</p>
<p>{description}</p>
</div>

<div class="right">
<h2>Secure Sign In</h2>
<p>Access your personalised dashboard and manage your service preferences.</p>

<form onsubmit="return false;">
<label>Email address or mobile number</label>
<input type="email" disabled placeholder="demo.user@example.com">

<label>Password</label>
<input type="password" disabled placeholder="Disabled for safety">

<button type="button" disabled>Continue Securely</button>
</form>

<div class="demo">
DEMO ONLY - Fictional AI-generated phishing-style page. Disabled form. No real brand. No credential capture.
</div>
</div>
</section>
</div>
</body>
</html>
"""


services = [
    "Digital banking, loan guidance and customer service information.",
    "Online shopping support, delivery guidance and order information.",
    "Telecom plan information, broadband services and help articles.",
    "Insurance policy guidance, claims information and customer support.",
    "Travel booking information, itinerary support and service updates.",
    "Healthcare appointment guidance and patient information services.",
    "Education services, student helpdesk and academic information.",
    "Digital wallet information, transaction guidance and safety awareness."
]

warnings = [
    "Urgent: your online access will be suspended.",
    "Immediate verification required to continue service.",
    "Your digital account has been temporarily restricted.",
    "Security update required for your customer profile.",
    "Limited access detected. Verify your account now.",
    "Your payment profile requires immediate confirmation."
]

headlines = [
    "A smarter and safer way to manage your digital services across India.",
    "Review your account preferences, service updates and protection settings.",
    "Experience seamless access to your personalised financial dashboard.",
    "Manage your digital identity, security preferences and support requests.",
    "A modern customer portal designed for secure online convenience."
]

descriptions = [
    "This fictional page uses polished language and modern layout patterns to represent AI-generated web content for research purposes.",
    "The design includes realistic content structure, dashboard-style messaging and security-focused microcopy for classification testing.",
    "This static webpage helps evaluate whether machine-learning models can distinguish polished synthetic pages from other webpage classes.",
    "The page is fully offline, non-functional and created only as a safe academic artefact for phishing-detection research."
]


# Remove old generated files only if they follow our naming pattern
for folder in FOLDERS:
    for file in folder.glob("*.html"):
        file.unlink()


for i in range(1, 51):
    brand = indian_legitimate_brands[(i - 1) % len(indian_legitimate_brands)]
    html = legitimate_template.format(
        brand=f"{brand} {i}",
        service_text=random.choice(services)
    )
    file_path = BASE_DIR / "legitimate" / f"legitimate_{i:03d}.html"
    file_path.write_text(html, encoding="utf-8")


for i in range(1, 51):
    brand = traditional_phishing_brands[(i - 1) % len(traditional_phishing_brands)]
    html = traditional_template.format(
        brand=f"{brand} {i}",
        warning_text=random.choice(warnings)
    )
    file_path = BASE_DIR / "traditional_phishing" / f"traditional_{i:03d}.html"
    file_path.write_text(html, encoding="utf-8")


for i in range(1, 51):
    brand = ai_generated_brands[(i - 1) % len(ai_generated_brands)]
    html = ai_generated_template.format(
        brand=f"{brand} {i}",
        headline=random.choice(headlines),
        description=random.choice(descriptions)
    )
    file_path = BASE_DIR / "ai_generated_phishing" / f"ai_generated_{i:03d}.html"
    file_path.write_text(html, encoding="utf-8")


print("150 dummy Indian-context HTML webpages created successfully.")
print("50 legitimate pages")
print("50 traditional phishing-style pages")
print("50 AI-generated phishing-style pages")