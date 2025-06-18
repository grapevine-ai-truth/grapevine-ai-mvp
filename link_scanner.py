# link_scanner.py

import tldextract

def is_link_suspicious(url):
    """
    Checks if the given URL uses a known suspicious or shortened domain.
    Returns True if it should be flagged.
    """
    suspicious_domains = [
        "bit.ly", "tinyurl.com", "weird-domain.biz", "shady.link", "clickbait.com"
    ]
    ext = tldextract.extract(url)
    domain = f"{ext.domain}.{ext.suffix}"

    return domain.lower() in suspicious_domains
