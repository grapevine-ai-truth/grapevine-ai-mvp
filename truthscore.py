# truthscore.py

import re

def calculate_truth_score(message):
    """
    Assigns a credibility score (0–100) to a message based on its content.
    Penalizes common scammy phrases, excessive length, and presence of URLs.
    """
    score = 100
    red_flags = [
        "free", "click here", "act now", "guaranteed",
        "risk-free", "urgent", "limited time", "winner",
        "exclusive deal", "wire transfer", "unclaimed"
    ]

    # Penalize for red-flag language
    for keyword in red_flags:
        if keyword in message.lower():
            score -= 10

    # Penalize for excessive length
    if len(message) > 500:
        score -= 10

    # Penalize for containing URLs
    if "http" in message or "www." in message:
        score -= 20

    return max(score, 0)
