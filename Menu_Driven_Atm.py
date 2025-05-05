def atm_system():
    balance = 10000  # Initial balance
    
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = int(input("Enter your choice (1-4): "))
        
        if choice == 1:
            print("Your current balance is ₹", balance)
        
        elif choice == 2:
            amount = float(input("Enter deposit amount: ₹"))
            if amount > 0:
                balance += amount
                print("₹", amount, "deposited successfully.")
                print("Updated balance: ₹", balance)
            else:
                print("Invalid deposit amount. Try again.")
        
        elif choice == 3:
            amount = float(input("Enter withdrawal amount: ₹"))
            if 0 < amount <= balance:
                balance -= amount
                print("₹", amount, "withdrawn successfully.")
                print("Updated balance: ₹", balance)
            elif amount > balance:
                print("Insufficient balance!")
            else:
                print("Invalid withdrawal amount. Try again.")
        
        elif choice == 4:
            print("Thank you for using the ATM. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

# Run the ATM system
atm_system()
