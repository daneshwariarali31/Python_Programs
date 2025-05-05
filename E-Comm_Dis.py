# Take user input for purchase amount
amount = float(input("Enter your purchase amount: ₹"))

# Apply discount based on conditions
if amount > 5000:
    discount = 0.20 * amount  # 20% discount
elif amount >= 3000:
    discount = 0.15 * amount  # 15% discount
elif amount >= 1000:
    discount = 0.10 * amount  # 10% discount
else:
    discount = 0  # No discount

# Calculate final amount to pay
final_amount = amount - discount

# Display the results
print(f"\n🛍 Original Price: ₹{amount:.2f}")
print(f"🎉 Discount Applied: ₹{discount:.2f}")
print(f"💰 Final Payable Amount: ₹{final_amount:.2f}")
