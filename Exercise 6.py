def is_palindrome(number):
    str_number = str(number)
    reversed_number = str_number[::-1]
    # Compare the original and reversed strings
    return str_number == reversed_number

# Example usage
num = 121

if is_palindrome(num):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")
