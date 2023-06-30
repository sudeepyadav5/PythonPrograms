import re


def is_valid_password(password):
    # Check if password contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # Check if password contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # Check if password contains at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    # Check if password contains at least one number
    if not re.search(r'\d', password):
        return False

    # If all conditions are met, return True
    return True


# Test the function with different passwords
"""passwords = [
    'abcAde123$',  # Valid password
    'abcde123',  # Invalid - missing special char
    'ABCDE123$',  # Invalid - missing lowercase char
    'abcde$$$$',  # Invalid - missing number
    'ABC1234$',  # Invalid - missing lowercase char
    'abcde 123$',  # Invalid - contains whitespace
    'ABCaD#E123'  # Valid password
]"""
pwd = input("Enter Password")
passwords = [pwd]

for password in passwords:
    if is_valid_password(password):
        print(f"{password} is a valid password")
    else:
        print(f"{password} is an invalid password, Password Should be attlist 1 lower case, 1 upper case, 1 numeric "
              f"and 1 special character")
