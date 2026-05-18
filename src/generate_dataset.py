from pathlib import Path
import random

# Create folders if not exist
legit_path = Path("data/legitimate")
phishing_path = Path("data/ai_generated_phishing")

legit_path.mkdir(parents=True, exist_ok=True)
phishing_path.mkdir(parents=True, exist_ok=True)


# -----------------------------
# Legitimate page generator
# -----------------------------
def generate_legit_page(index):
    titles = [
        "Digital Services Portal",
        "Secure Customer Dashboard",
        "Online Banking Services",
        "E-Commerce Platform",
        "Payment Gateway Services"
    ]

    services = [
        "Account Management",
        "Bill Payments",
        "Order Tracking",
        "Customer Support",
        "Profile Settings"
    ]

    return f"""
<!DOCTYPE html>
<html>
<head>
<title>{random.choice(titles)}</title>
</head>
<body style="font-family:Arial;background:#f4f7fb;padding:40px;">

<h1>{random.choice(titles)}</h1>

<p>Welcome to our secure platform. Access services and manage your account easily.</p>

<h3>Services</h3>
<ul>
  <li>{random.choice(services)}</li>
  <li>{random.choice(services)}</li>
  <li>{random.choice(services)}</li>
</ul>

<h3>Login</h3>
<input type="text" placeholder="User ID"><br><br>
<input type="password" placeholder="Password"><br><br>

<button>Login</button>

<p style="color:#666;">Your security is our priority.</p>

</body>
</html>
"""


# -----------------------------
# Phishing page generator
# -----------------------------
def generate_phishing_page(index):
    alerts = [
        "Urgent action required",
        "Account suspended",
        "Security alert",
        "Verify immediately",
        "Unusual activity detected"
    ]

    actions = [
        "Verify your account",
        "Update your details",
        "Confirm your identity",
        "Reset your password",
        "Validate your information"
    ]

    return f"""
<!DOCTYPE html>
<html>
<head>
<title>Security Verification</title>
</head>
<body style="font-family:Arial;background:#fff3f3;padding:40px;">

<h2>{random.choice(alerts)}</h2>

<p>Your account has been temporarily restricted due to suspicious activity.</p>

<p><strong>{random.choice(actions)}</strong></p>

<input type="email" placeholder="Email"><br><br>
<input type="password" placeholder="Password"><br><br>
<input type="text" placeholder="OTP"><br><br>

<button>Verify Now</button>

<p style="color:red;">Failure to act within 24 hours may result in account suspension.</p>

<p>DEMO ONLY — Synthetic phishing page</p>

</body>
</html>
"""


# -----------------------------
# Generate files
# -----------------------------
print("Generating legitimate pages...")
for i in range(50):
    file = legit_path / f"legit_auto_{i+1}.html"
    file.write_text(generate_legit_page(i), encoding="utf-8")

print("Generating phishing pages...")
for i in range(50):
    file = phishing_path / f"phishing_auto_{i+1}.html"
    file.write_text(generate_phishing_page(i), encoding="utf-8")

print("✅ 50 Legitimate + 50 Phishing pages generated successfully!")