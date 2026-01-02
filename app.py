from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = "504f3e72c49a2b9dc88107668b5483a61c82c8e647b30e31eec2c9d30d7a37ab"

# path to store email addresses (simple, file based - can be changed)
EMAIL_FILE = "emails.txt"

# countdown to 12:00am est february 1st, 2026
RELEASE_DATETIME = datetime(2026, 2, 1, 0, 0, 0)

# email signup
@app.route("/", methods=["GET", "POST"])
def landing():
    if request.method == "POST":
        email = request.form.get("email", "").strip()

        if not email:
            flash("Email can't be empty.", "error")
        elif "@" not in email:
            flash("Enter a valid email address.", "error")
        else:
            save_email(email)
            flash("You're locked in. Watch your inbox.", "success")
            return redirect(url_for("landing"))
        
    # send the release timestamp for live countdown with JavaScript
    release_timestamp = int(RELEASE_DATETIME.timestamp() * 1000) # milliseconds

    return render_template(
        "landing.html",
        release_timestamp=release_timestamp
    )

def save_email(email):
    # make sure file exists then appends file
    existing = set()
    if os.path.exists(EMAIL_FILE):
        with open(EMAIL_FILE, "r", encoding="utf-8") as f:
            for line in f:
                existing.add(line.strip().lower())

    if email.lower() not in existing:
        with open(EMAIL_FILE, "a", encoding="utf-8") as f:
            f.write(email + "\n")

if __name__ == "__main__":
    app.run(debug=True)