num = int(input("Enter a number: "))  # Take input from user
original_num = num  # Store the original number
reverse_num = 0  # Variable to store the reversed number

while num > 0:  # Loop until num becomes 0
    digit = num % 10  # Extract the last digit
    reverse_num = (reverse_num * 10) + digit  # Append digit to reversed number
    num = num // 10  # Remove last digit from num

# Check if the original number and reversed number are the same
if original_num == reverse_num:
    print(original_num, "is a palindrome number")
else:
    print(original_num, "is not a palindrome number")
