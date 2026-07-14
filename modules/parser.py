import re

def extract_entities(text):
    entities = {
        "email": re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text),
        "phone": re.findall(r'\+?\d[\d\s-]{8,}\d', text),
        "invoice_id": re.findall(r'INV-\d+', text, re.IGNORECASE),
        "ticket_id": re.findall(r'TCK-\d+', text, re.IGNORECASE),
        "amount": re.findall(r'[₹$]\s?\d+(?:,\d{3})*(?:\.\d{2})?', text),
        "order_id": re.findall(r'ORD-\d+', text, re.IGNORECASE)
    }

    return entities