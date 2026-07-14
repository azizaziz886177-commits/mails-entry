for email_data in emails:

    cleaned_body = clean_text(email_data["body"])
    category = classify_email(cleaned_body)
    entities = extract_entities(email_data["body"])

    phishing = detect_phishing(
        email_data["subject"],
        email_data["body"],
        email_data["sender"]
    )

    print("Risk Level :", phishing["risk"])
    print("Risk Score :", phishing["score"])
    print("Reasons    :", phishing["reasons"])

    print("=" * 60)
    print("Sender :", email_data["sender"])
    print("Subject :", email_data["subject"])
    print("Category :", category)
    print("Date :", email_data["date"])
    print("Emails :", entities["email"])
    print("Phone :", entities["phone"])
    print("Invoice IDs :", entities["invoice_id"])
    print("Ticket IDs :", entities["ticket_id"])
    print("Amounts :", entities["amount"])
    print("Order IDs :", entities["order_id"])
    print("Cleaned Body :", cleaned_body[:200])

    processed_data.append({
        "email_id": email_data["email_id"],
        "sender": email_data["sender"],
        "subject": email_data["subject"],
        "date": email_data["date"],
        "category": category,
        "body_preview": cleaned_body[:200]
    })

    entity_data.append({
        "email_id": email_data["email_id"],
        "phone_number": ", ".join(entities["phone"]),
        "invoice_id": ", ".join(entities["invoice_id"]),
        "ticket_id": ", ".join(entities["ticket_id"]),
        "amount": ", ".join(entities["amount"]),
        "order_id": ", ".join(entities["order_id"])
    })