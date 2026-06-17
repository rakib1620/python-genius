# 1. TODO: Capture inputs from user (Name, Age, Developer Status)
name = input("Please enter your name:\n")
age = int(input("Please enter your age:\n"))

# Convert input to lowercase to handle variations like 'Yes', 'YES', etc.
is_developer = input("Are you a developer? (yes/no): ").strip().lower()


# 2. TODO: Evaluate conditional logic to determine the clearance tier
if age < 18:
    clearance_tier = "Tier 3: Guest Access"

elif age >= 18 and is_developer == "yes":
    clearance_tier = "Tier 1: Admin Infrastructure Access"

else:
    clearance_tier = "Tier 2: Standard Executive Access"


# 3. TODO: Print out the final profile card using an f-string
print("\n" + "="*35)
print("        --- PROFILE CARD ---")
print("="*35)
print(f"Name:               {name}")
print(f"Age:                {age}")
print(f"Developer Status:   {is_developer.capitalize()}")
print(f"Assigned Clearance: {clearance_tier}")
print("="*35)