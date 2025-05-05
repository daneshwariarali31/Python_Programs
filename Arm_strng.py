num = int(input("Enter a number: "))  # Get input from user
original_num = num  # Store original number
sum_of_cubes = 0  # Initialize sum

while num > 0:
    digit = num % 10  # Extract last digit
    sum_of_cubes += digit ** 3  # Cube the digit and add to sum
    num = num // 10  # Remove last digit

# Check if the sum of cubes equals the original number
if original_num == sum_of_cubes:
    print(original_num, "is an Armstrong number")
else:
    print(original_num, "is not an Armstrong number")
