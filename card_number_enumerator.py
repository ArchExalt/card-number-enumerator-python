# enumerate all the valid payment card numbers

from itertools import product

def luhn_check(card_number: str) -> bool:
    digits = [int(d) for d in reversed(card_number)]
    
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    
    total_sum = sum(digits)
    return total_sum % 10 == 0

def generate_possible_cards(partial_card_number: str):
    valid_count = 0  # Initialize the counter before any return statements

    if len(partial_card_number) != 16 or partial_card_number[0] not in "12345689":
        print("Invalid card number.")
        return

    print("Valid card numbers:")
    
    num_wildcards = partial_card_number.count('*')
    
    for replacement in product('0123456789', repeat=num_wildcards):
        candidate = list(partial_card_number)
        replacement_index = 0
        
        for i, ch in enumerate(candidate):
            if ch == '*':
                candidate[i] = replacement[replacement_index]
                replacement_index += 1
        
        candidate_number = ''.join(candidate)
        
        if luhn_check(candidate_number):
            print(candidate_number)
            valid_count += 1  # Increment the counter
    
    print(f"Enumeration completed. {valid_count} valid card number(s) found.")
    
partial_card_number = input("Enter the payment card number marking unknown digits with asterisks: ")
generate_possible_cards(partial_card_number)

input("Press Enter to exit...")
