#Largest of Three numbers
num1=int(input("Enter a first number:"))
num2=int(input("Enter a second number:"))
num3=int(input("Enter a third number:"))

if num1>num2 and num1>num3:
    print(f"The Largest number is {num1}")

elif num2>num1 and num2>num3:
    print(f"The Largest number is {num2}")
    
else:
    print(f"The Largest number is {num3}")
