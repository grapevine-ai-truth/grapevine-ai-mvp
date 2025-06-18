# utils.py

def clean_text(text):
    """
    Removes extra whitespace and newline characters from a message.
    """
    return text.strip().replace('\n', ' ').replace('\r', '')
