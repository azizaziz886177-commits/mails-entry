import imaplib
import json

def connect_gmail():
    with open("config.json", "r") as file:
        config = json.load(file)

    email = config["email"]
    password = config["app_password"]

    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(email, password)
        print("Gmail Connected Successfully")
        return mail

    except Exception as e:
        print("Connection Failed:", e)
        return None