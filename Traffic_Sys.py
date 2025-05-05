light = input("Enter the traffic light color (Red/Yellow/Green): ").strip().lower()

if light == "red":
    print("🚦 RED Light - STOP!")
elif light == "yellow":
    print("⚠ YELLOW Light - GET READY!")
elif light == "green":
    print("✅ GREEN Light - GO!")
else:
    print("❌ Invalid input! Please enter Red, Yellow, or Green.")
