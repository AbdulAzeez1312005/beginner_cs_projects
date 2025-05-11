def check_urgency(email_body):
    """Checks for keywords indicating urgency."""
    urgency_keywords = ["immediately", "act now", "within 24 hours", "urgent", "important"]
    urgency_count = 0
    for keyword in urgency_keywords:
        if keyword.lower() in email_body.lower():
            urgency_count += 1

    if urgency_count > 2: # You can adjust this threshold
        print(f"High level of urgency detected ({urgency_count} urgency keywords). Be cautious.")
    elif urgency_count > 0:
        print(f"Some urgency indicators found ({urgency_count} keywords).")

def basic_grammar_check(email_body):
    """Checks for a few common misspellings (very basic)."""
    common_misspellings = ["recieve", "adress", "securty", "loggin", "pleas"]
    misspelling_found = False
    for word in common_misspellings:
        if word in email_body.lower():
            print(f"Potential misspelling found: '{word}'")
            misspelling_found = True

    if misspelling_found:
        print("Possible signs of unprofessionalism, be cautious.")

# --- How to use ---
if __name__ == "__main__":
    print("Enter the email body text (copy and paste):")
    email_text = input()
    print("\n--- Urgency Check ---")
    check_urgency(email_text)
    print("\n--- Basic Grammar Check ---")
    basic_grammar_check(email_text)
