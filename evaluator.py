import re
import string

def evaluate_password_strength(password):
    score = 0
    remarks = []

    if len(password) >= 8:
        score += 2
        remarks.append("Good length")
    elif len(password) >= 5:
        score += 1
        remarks.append("Moderate length")
    else:
        remarks.append("Too short")

    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    common_patterns = ["123", "abc", "password", "qwerty"]
    if any(pattern in password.lower() for pattern in common_patterns):
        score -= 2
        remarks.append("Contains common pattern")

    if score >= 6:
        strength = "Strong"
    elif score >= 4:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, remarks
