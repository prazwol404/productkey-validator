import sys
sys.stdout.reconfigure(encoding='utf-8')

import re

def validate_format(product_key):
    pattern = r"^[A-Z0-9]{5}-[A-Z0-9]{5}-[A-Z0-9]{5}-[A-Z0-9]{5}$"
    return bool(re.match(pattern, product_key))

def luhn_checksum(product_key):
    key_digits = product_key.replace("-", "")
    
    converted_digits = []
    for char in key_digits:
        if char.isdigit():
            converted_digits.append(int(char))
        else:
            converted_digits.append(ord(char) - ord('A') + 1)

    total = 0
    reverse_digits = converted_digits[::-1]

    for i, digit in enumerate(reverse_digits):
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    return total % 10 == 0

def validate_product_key(product_key):
    if not validate_format(product_key):
        return f"❌ Invalid format: {product_key}"
    
    if not luhn_checksum(product_key):
        return f"❌ Invalid checksum: {product_key}"
    
    return f"✅ Valid product key: {product_key}"

keys = [
    
    "5JJL8-P706J-UGOH4W451T"
]

for key in keys:
    print(validate_product_key(key))
