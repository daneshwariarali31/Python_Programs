a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if a+b>c and b+c>a and c+a>b:
    print("Traingle is Valid")

else:
    print("Traingle is Not Valid")