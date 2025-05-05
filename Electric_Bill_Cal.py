# Take user input for electricity units consumed
units = int(input("Enter the number of units consumed: "))

# Calculate bill based on unit slabs
if units <= 100:
    bill = units * 5  # ₹5 per unit for first 100 units
elif units <= 300:
    bill = (100 * 5) + ((units - 100) * 8)  # First 100 units @ ₹5, remaining @ ₹8
else:
    bill = (100 * 5) + (200 * 8) + ((units - 300) * 10)  # First 100 @ ₹5, next 200 @ ₹8, remaining @ ₹10

# Display the total electricity bill
print(f"\n💡 Total Electricity Bill: ₹{bill:.2f}")
