def is_number_palindrome(num):
    # Negative numbers are not palindromes (e.g., -121 reversed is 121-)
    if num < 0:
        return False

    original = num
    reversed_num = 0

    while num > 0:
        last_digit = num % 10
        reversed_num = (reversed_num * 10) + last_digit
        num //= 10

    return original == reversed_num


# Test cases
print(is_number_palindrome(12321))  # True
print(is_number_palindrome(456))  # False
