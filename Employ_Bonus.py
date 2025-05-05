salary = float(input("Enter your salary: ₹"))
years_of_service = int(input("Enter your years of service: "))

if years_of_service > 5:  # Checking if the employee has worked for more than 5 years
    bonus = 0.10 * salary  # 10% bonus
    print("Congratulations! You get a bonus of ₹", bonus)
    print("Total salary after bonus: ₹", salary + bonus)
else:
    print("Sorry, no bonus. You need to work more than 5 years to get a bonus.")
