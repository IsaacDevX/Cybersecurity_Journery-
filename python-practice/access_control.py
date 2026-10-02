ip_in_whitelist = True
is_account_locked = False
failed_attempts = 2

if ip_in_whitelist and not is_account_locked and failed_attempts < 5:
    print("Access granted")
else:
    print("Access denied")
