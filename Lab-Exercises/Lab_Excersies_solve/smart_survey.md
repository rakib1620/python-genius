# The Smart Survey Onboarding Engine

This is a Python-based entry portal script designed for an automated processing system. The script interviews a user, captures their profile information, evaluates their clearance tier based on age and developer status, and generates a personalized configuration profile card.

## 🚀 Learning Objectives
- Input capturing using `input()` and type casting (`int`).
- Conditional logic implementation using `if-elif-else` and logical operators (`and`).
- String manipulation and output formatting using **F-strings** and string methods (`.lower()`, `.strip()`, `.capitalize()`).

---

## 📋 Clearance Tier Logic Rules

The engine evaluates access tiers based on the following strict criteria:

| Criteria | Assigned Tier | Access Level |
| :--- | :--- | :--- |
| Age is under 18 | **Tier 3** | Guest Access |
| Age is 18 or older **AND** a Developer | **Tier 1** | Admin Infrastructure Access |
| Age is 18 or older **AND** NOT a Developer | **Tier 2** | Standard Executive Access |

---

## 🛠️ Features Included
- **Robust Input Handling:** Uses `.strip().lower()` to handle user input variations (e.g., ` YES `, `Yes`, `yes`).
- **Clean Layout:** Automatically formats the terminal output into a well-aligned **Profile Card** using dynamic string repetition (`*35`).

---

## 💻 How to Run the Script

1. Make sure you have Python installed on your system.
2. Clone this repository or navigate to your project directory.
3. Run the script using the terminal:
   ```bash
   python smart_survey.py