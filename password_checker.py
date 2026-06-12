import re

def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Too short (use 8+ characters)")
    
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add an uppercase letter")
    
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add a lowercase letter")
    
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add a number")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Add a special character (!@#$%^&*)")
    
    levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong", "Excellent"]
    print(f"Strength: {levels[score]}")
    if feedback:
        print("Suggestions:")
        for f in feedback:
            print(f"- {f}")

# Test it
password = input("Enter a password to check: ")
check_password_strength(password)
