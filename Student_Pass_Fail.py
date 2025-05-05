# Take the number of subjects from the user
num_subjects = int(input("Enter the number of subjects: "))

# List to store marks of each subject
marks = []

# Take marks input for each subject
for i in range(num_subjects):
    mark = float(input(f"Enter marks for Subject {i+1}: "))
    marks.append(mark)

# Check if the student passes in all subjects
if all(mark >= 40 for mark in marks):  # Using all() function to check all conditions
    print("\n🎉 Congratulations! You have PASSED all subjects.")
else:
    print("\n❌ Sorry, you have FAILED. You must score at least 40% in all subjects.")
