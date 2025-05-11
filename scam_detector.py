def detect_suspicious_keywords(email_body):
    """Checks if the email body contains suspicious keywords."""
    suspicious_keywords = [
        "urgent action required",
        "verify your account",
        "security alert",
        "click here immediately",
        "prize winner",
        "inheritance",
        "IRS notice",
        "your account will be suspended",
        "limited time offer",
        "free gift"
    ]
    found_keywords = []
    for keyword in suspicious_keywords:
        if keyword.lower() in email_body.lower():
            found_keywords.append(keyword)

    if found_keywords:
        print("Potential Scam/Phishing Keywords Found:")
        for keyword in found_keywords:
            print(f"- {keyword}")
        print("Be cautious with this email.")
    else:
        print("No obvious suspicious keywords found.")

# --- How to use ---
if __name__ == "__main__":
    print("Enter the email body text (copy and paste):")
    email_text = input()
    detect_suspicious_keywords(email_text)
