# Mini Project: User Info & Age Category Checker

# Step 1: Take user input
name = input("Enter your name: ")
age_input = input("Enter your age: ")
location = input("Enter your location: ")

# Step 2: Try to convert age to a number
try:
    age = int(age_input)
except:
    print("Please enter a valid number for age.")
    exit()

# Step 3: Show user summary
print("\n--- User Summary ---")
print("Name     :", name)
print("Age      :", age)
print("Location :", location)

# Step 4: Determine age category
print("\n--- Age Category ---")
if age < 18:
    print("You are a Minor.")
elif age < 60:
    print("You are an Adult.")
else:
    print("You are a Senior Citizen.")