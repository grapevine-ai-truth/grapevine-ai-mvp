import re

# Common red-flag words or phrases often used in scams or manipulative content
SUSPICIOUS_KEYWORDS = [
    "urgent", "immediately", "limited time", "act now", "verify your account",
    "click here", "risk-free", "guaranteed", "winner", "you’ve been selected",
    "update your payment", "unauthorized access", "congratulations", "free trial"
]

def calculate_truth_score(message: str) -> dict:
    lowered = message.lower()

    keyword_hits = [kw for kw in SUSPICIOUS_KEYWORDS if kw in lowered]
    num_flags = len(keyword_hits)

    length_penalty = 0
    if len(message) < 30:
        length_penalty = 15  # Very short messages may lack context
    elif len(message) > 1000:
        length_penalty = 5   # Very long messages may try to overwhelm

    base_score = 100 - (num_flags * 10) - length_penalty
    score = max(0, min(base_score, 100))

    return {
        "score": score,
        "flags": keyword_hits
    }
