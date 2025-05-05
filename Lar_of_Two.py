num1=int(input("Enter first number:"))
num2=int(input("Enter second number"))

if num1>num2:
    print(f"The {num1} is Larger")
    largest=num1
    
else:
    print(f"The {num2} is Larger")
    largest=num2
print(f"The Largest of Two number is {largest}")