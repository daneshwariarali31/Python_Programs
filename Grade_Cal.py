perc = float(input("Enter your percentage: "))

# Checking for valid input range
if perc < 0 or perc > 100:
    print("Invalid input! Please enter a percentage between 0 and 100.")
elif perc >= 90:
    print("Your Grade is A")
elif perc >= 80:
    print("Your Grade is B")
elif perc >= 70:
    print("Your Grade is C")
elif perc >= 60:
    print("Your Grade is D")
else:
    print("You have failed. Better luck next time!")
