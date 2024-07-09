import re

def check_password_complexity(password):
    # Define the criteria for a strong password
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r"[A-Z]", password)
    lower_criteria = re.search(r"[a-z]", password)
    digit_criteria = re.search(r"\d", password)
    special_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    # Check if all criteria are met
    if (length_criteria and upper_criteria and lower_criteria 
            and digit_criteria and special_criteria):
        return "Strong"
    elif (length_criteria and upper_criteria and lower_criteria 
            and (digit_criteria or special_criteria)):
        return "Moderate"
    else:
        return "Weak"

def main():
    print("Password Complexity Checker")
    password = input("Enter a password to check its complexity: ").strip()
    
    complexity = check_password_complexity(password)
    print(f"Password complexity: {complexity}")

if __name__ == "__main__":
    main()
