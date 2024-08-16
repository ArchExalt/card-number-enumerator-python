# check whether the payment card number is valid or not

def luhn_check(card_number: str) -> str:
    if len(card_number) != 16 or card_number[0] not in "12345689":
        return "Invalid card number."

    # Reverse the card number and convert it to a list of integers
    digits = [int(d) for d in reversed(card_number)]

    # Double every second digit from the right (starting from the second digit)
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
            
    total_sum = sum(digits)
    return "valid" if total_sum % 10 == 0 else "not valid"


card_number = input("Enter the payment card number: ")
is_valid = luhn_check(card_number)
print(f"Card number is {is_valid}.")

input("Press Enter to exit...")
