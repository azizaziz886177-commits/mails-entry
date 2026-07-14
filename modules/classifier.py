def classify_email(text):
    text = text.lower()

    categories = {
        "Invoice": ["invoice", "payment", "due", "receipt", "bill"],
        "Support": ["issue", "error", "problem", "help", "support"],
        "Sales Lead": ["pricing", "quote", "demo", "interested", "buy"],
        "HR": ["resume", "application", "cv", "interview", "job"],
        "Internal": ["meeting", "team", "project", "schedule"],
        "Spam": ["lottery", "winner", "claim", "offer", "free"]
    }

    scores = {}

    for category, keywords in categories.items():
        scores[category] = sum(text.count(word) for word in keywords)

    if max(scores.values()) == 0:
        return "General"

    return max(scores, key=scores.get)