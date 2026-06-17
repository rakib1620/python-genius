# How I Solved It: Dynamic Access Clearance Profiler

This documentation explains how I built a dynamic user profiling script in Python that evaluates input flags to assign system clearance tiers.

---

## 🧭 The Problem
Security and access control systems need to evaluate multiple user parameters (like age and professional role) before granting permissions. The objective was to capture user inputs, process them through conditional logic gates, and output a structured profile summary card.

---

## 🛠️ Step-by-Step Solution

### Step 1: Input Capture and Sanitization
I captured the user's name, age, and professional status using the `input()` function. To ensure data consistency, the age input is wrapped in `int()`, and the developer status is sanitized using `.strip().lower()` to handle variations in user formatting (e.g., "  YES ").

### Step 2: Multi-Branch Conditional Logic
I implemented an `if-elif-else` control flow to check the conditions sequentially:
1. **Underage Gate (`age < 18`):** Instantly flags the profile for guest access regardless of other answers.
2. **Admin Gate (`age >= 18 and is_developer == "yes"`):** Verifies adulthood and role alignment to grant infrastructure access.
3. **Fallback Gate (`else`):** Catches all other standard variations.

### Step 3: Formatted Output Rendering
Using Python **f-strings**, the script dynamically injects the processed states into a structured visual text terminal card, applying `.capitalize()` to the developer flag for clean presentation.

---

## 💻 Final Script Structure

```python
# 1. Capture inputs from user (Name, Age, Developer Status)
name = input("Please enter your name:\n")
age = int(input("Please enter your age:\n"))
is_developer = input("Are you a developer? (yes/no): ").strip().lower()

# 2. Evaluate conditional logic to determine the clearance tier
if age < 18:
    clearance_tier = "Tier 3: Guest Access"
elif age >= 18 and is_developer == "yes":
    clearance_tier = "Tier 1: Admin Infrastructure Access"
else:
    clearance_tier = "Tier 2: Standard Executive Access"

# 3. Print out the final profile card using an f-string
print("\n" + "="*35)
print("        --- PROFILE CARD ---")
print("="*35)
print(f"Name:               {name}")
print(f"Age:                {age}")
print(f"Developer Status:   {is_developer.capitalize()}")
print(f"Assigned Clearance: {clearance_tier}")
print("="*35)

Please enter your name:
Md Rakib Hossain
Please enter your age:
28
Are you a developer? (yes/no): yes

===================================
        --- PROFILE CARD ---
===================================
Name:               Md Rakib Hossain
Age:                28
Developer Status:   Yes
Assigned Clearance: Tier 1: Admin Infrastructure Access
===================================