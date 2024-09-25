def binary_to_decimal(binary_str):
    # Initialize the decimal result
    decimal_value = 0
    
    # Iterate through each character in the binary string
    for index, digit in enumerate(reversed(binary_str)):
        # Convert the character to an integer and calculate its decimal value
        decimal_value += int(digit) * (2 ** index)
    
    return decimal_value

# Example usage
binary_number = "1101"  # Binary for decimal 13
decimal_number = binary_to_decimal(binary_number)
print(f"Binary: {binary_number} => Decimal: {decimal_number}")