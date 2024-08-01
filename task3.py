import re

def check_password_strength(password):
    """
    Check the strength of a given password based on defined criteria.
    
    Args:
    password (str): The password to be checked.

    Returns:
    dict: A dictionary with the strength assessment and feedback.
    """
    feedback = []

    # Check length
    if len(password) < 8:
        feedback.append("Password must be at least 8 characters long.")

    # Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        feedback.append("Password must contain at least one uppercase letter.")

    # Check for lowercase letters
    if not re.search(r'[a-z]', password):
        feedback.append("Password must contain at least one lowercase letter.")

    # Check for numbers
    if not re.search(r'[0-9]', password):
        feedback.append("Password must contain at least one number.")

    # Check for special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("Password must contain at least one special character.")

    # Determine strength
    if len(feedback) == 0:
        strength = "Strong"
    elif len(feedback) <= 2:
        strength = "Moderate"
    else:
        strength = "Weak"

    return {
        "strength": strength,
        "feedback": feedback
    }

def main():
    print("Password Complexity Checker")
    password = input("Enter your password: ")

    result = check_password_strength(password)

    print(f"Password Strength: {result['strength']}")
    if result['feedback']:
        print("Feedback:")
        for message in result['feedback']:
            print(f"- {message}")


if __name__ == "__main__":
    main()
