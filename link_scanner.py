import re
import tldextract

# Known shady patterns or suspicious TLDs (top-level domains)
SUSPICIOUS_TLDS = ['.xyz', '.top', '.ru', '.tk', '.info', '.buzz', '.club']
SUSPICIOUS_KEYWORDS = ['login', 'verify', 'update', 'free-gift', 'confirm', 'secure', 'claim']

def extract_links(message: str) -> list:
    # Regex pattern to find URLs
    url_pattern = r'(https?://[^\s]+)'
    return re.findall(url_pattern, message)

def analyze_link(link: str) -> dict:
    domain_info = tldextract.extract(link)
    full_domain = f"{domain_info.domain}.{domain_info.suffix}"
    flags = []

    # Check for sketchy domain extensions
    for tld in SUSPICIOUS_TLDS:
        if full_domain.endswith(tld):
            flags.append(f"suspicious TLD ({tld})")

    # Check for phishing-like keywords in the URL
    for word in SUSPICIOUS_KEYWORDS:
        if word in link.lower():
            flags.append(f"contains '{word}'")

    return {
        "url": link,
        "flags": flags,
        "is_suspicious": len(flags) > 0
    }

def scan_links(message: str) -> list:
    links = extract_links(message)
    return [analyze_link(link) for link in links]
