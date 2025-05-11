from urllib.parse import urlparse

def get_domain(url):
    """Extracts the domain name from a URL."""
    try:
        parsed_url = urlparse(url)
        return parsed_url.netloc
    except:
        return None

def check_link_suspiciousness(url, trusted_domains):
    """Checks if the domain of a URL is in the list of trusted domains."""
    domain = get_domain(url)
    if domain:
        if domain in trusted_domains:
            print(f"The domain '{domain}' appears to be trusted.")
        else:
            print(f"Warning: The domain '{domain}' is not in the trusted list.")
    else:
        print("Invalid URL provided.")

# --- How to use ---
if __name__ == "__main__":
    trusted_domains = ["yourbank.com", "paypal.com", "gmail.com", "outlook.com"] # Add your trusted domains
    print("Enter a URL from the email:")
    link_url = input()
    check_link_suspiciousness(link_url, trusted_domains)
