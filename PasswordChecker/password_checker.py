# Password Strength Checker
import re

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Add at least one special character.")

    if strength <= 2:
        level = "Weak"
    elif strength in (3, 4):
        level = "Medium"
    else:
        level = "Strong"

    return level, feedback


if __name__ == "__main__":
    pwd = input("Enter password to check: ")
    level, suggestions = check_password_strength(pwd)
    print(f"Password Strength: {level}")
    if suggestions:
        print("Suggestions:")
        for s in suggestions:
            print("-", s)
