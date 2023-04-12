import re

def validate_password(password):
    if len(password) < 6 or len(password) > 12:
        return False
    if not re.search('[a-zA-Z]', password) or not re.search('[0-9]', password):
        return False
    if not re.search('[@$#]', password):
        return False
    return True

# Example usage:
password = input("Enter your password: ")
if validate_password(password):
    print("Valid password!")
else:
    print("Invalid password.")
