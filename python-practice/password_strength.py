# password_strength.py
#
# A simple password strength checker.
#
# What it does:
#   Takes a password as input and checks if it meets the
#   minimum length requirement (8 or more characters).
#
# Returns:
#   True  → password is at least 8 characters
#   False → password is under 8 characters
#
# Author: Ikehi Isaac
# Date: October 2026


def check_password_strength(password):
    """
    Check if a password meets minimum length requirements.

    Args:
        password (str): The password to check.

    Returns:
        bool: True if 8+ characters, False otherwise.
    """
    if len(password) >= 8:
        return True
    else:
        return False


# Test the function with sample passwords
if __name__ == "__main__":
    print("Testing password strength checker:")
    print("------------------------------")
    print("'abc123'         ->", check_password_strength("abc123"))
    print("'SecurePass2026' ->", check_password_strength("SecurePass2026"))
    print("''               ->", check_password_strength(""))
    print("'12345678'       ->", check_password_strength("12345678"))
