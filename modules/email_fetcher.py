import email
from email.header import decode_header

def fetch_emails(mail, max_emails=10):
    emails = []

    mail.select("INBOX")

    status, messages = mail.search(None, "ALL")

    email_ids = messages[0].split()

    latest_ids = email_ids[-max_emails:]

    for eid in reversed(latest_ids):
        status, msg_data = mail.fetch(eid, "(RFC822)")

        for response in msg_data:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])

                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding or "utf-8", errors="ignore")

                sender = msg.get("From")
                date = msg.get("Date")

                body = ""

                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True).decode(errors="ignore")
                            break
                else:
                    body = msg.get_payload(decode=True).decode(errors="ignore")

                emails.append({
                    "email_id": eid.decode(),
                    "sender": sender,
                    "subject": subject,
                    "date": date,
                    "body": body
                })

    return emails