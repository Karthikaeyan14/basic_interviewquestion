def reverse_number_math(num):
    sign = -1 if num < 0 else 1
    num = abs(num)
    reversed_num = 0

    while num > 0:
        last_digit = num % 10  # Extract the last digit
        reversed_num = (reversed_num * 10) + last_digit  # Append it to the result
        num = num // 10  # Remove the last digit from the number

    return sign * reversed_num


# Test cases
print(reverse_number_math(12345))  # Output: 54321
print(reverse_number_math(-987))  # Output: -789


