# Conditional Statements (if, elif, else)

age = input("Enter your age: ")
if age < 18:
    print("You are a minor.")

elif age >= 18:
    print("You can drive on road.")

elif age > 60:
    print("You are a senior citizen.")

else:
    print("You are not Eligible to drive on road.")