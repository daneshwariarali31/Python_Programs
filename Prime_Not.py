num = int(input("Enter a number: "))  # Take input from the user

if num < 2:  # Prime numbers start from 2
    print(num, "is not a prime number")
else:
    for i in range(2, int(num ** 0.5) + 1):  # Loop from 2 to sqrt(num)
        if num % i == 0:  # If divisible by i, it's not prime
            print(num, "is not a prime number")
            break  # Exit loop immediately when a divisor is found
    else:
        print(num, "is a prime number")  # Runs only if loop completes without a break
