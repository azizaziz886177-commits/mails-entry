import re

def detect_phishing(subject, body, sender):
    """
    Detect phishing emails using simple keyword and pattern matching.
    Returns:
        risk_level (Low, Medium, High)
        reasons (list)
    """

    text = (subject + " " + body).lower()

    reasons = []
    score = 0

    # Suspicious keywords
    keywords = [
        "verify your account",
        "urgent",
        "click here",
        "login",
        "password",
        "bank",
        "credit card",
        "otp",
        "limited time",
        "winner",
        "lottery",
        "claim now",
        "free gift",
        "update account",
        "payment failed",
        "suspended",
        "confirm identity",
        "security alert"
    ]

    for word in keywords:
        if word in text:
            score += 2
            reasons.append(f"Keyword detected: {word}")

    # Suspicious links
    urls = re.findall(r'https?://\S+', body)

    if len(urls) > 0:
        score += 2
        reasons.append("Contains URL")

    # Shortened URLs
    short_domains = [
        "bit.ly",
        "tinyurl.com",
        "goo.gl",
        "t.co",
        "is.gd"
    ]

    for url in urls:
        for domain in short_domains:
            if domain in url:
                score += 3
                reasons.append("Shortened URL detected")

    # Many exclamation marks
    if body.count("!") >= 3:
        score += 1
        reasons.append("Too many exclamation marks")

    # ALL CAPS subject
    if subject.isupper() and len(subject) > 5:
        score += 1