# Taking user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

# Performing calculations based on the operator
if operator == '+':
    print(f"Result: {num1} + {num2} = {num1 + num2}")
    
elif operator == '-':
    print(f"Result: {num1} - {num2} = {num1 - num2}")
elif operator == '*':
    print(f"Result: {num1} * {num2} = {num1 * num2}")
elif operator == '/':
    if num2 != 0:  # Checking division by zero
        print(f"Result: {num1} / {num2} = {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator! Please enter one of (+, -, *, /).")
