from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    try:
        emails = pd.read_csv("output/processed_emails.csv").fillna("")
        return render_template(
            "dashboard.html",
            emails=emails.to_dict(orient="records")
        )
    except:
        return render_template("dashboard.html", emails=[])

@app.route("/analytics")
def analytics():
    return render_template("analytics.html")

@app.route("/email")
def email():
    return render_template("email.html")

if __name__ == "__main__":
    app.run(debug=True)