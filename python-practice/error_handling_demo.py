user_input = input("Enter a number: ")

try:
    number = int(user_input)
    print(f"[OK] Valid number: {number}")
except ValueError:
    print("[ERROR] Invalid input - please enter a number")
