# How I Solved It: Profile Text Normalization Pipeline

This is a simple guide showing how I cleaned messy user input text using Python string methods and loops.

---

## 🧭 The Problem
When users type data into a form, they often add extra spaces and mix up capital and small letters. Our goal was to take a list of messy text, clean it up, and save it into a new list called `sanitized_records`.

---

## 🛠️ Step-by-Step Solution

### Step 1: Using a For Loop
To clean every item inside the list, I used a standard `for` loop. Since our data is a Python List, we can loop through it directly like this:
```python
for item in raw_survey_inputs:
    cleaned_text = item.strip().lower()
    # Raw messy data from users
raw_survey_inputs = ["  ALICE SMITH ", " dhaka, BANGLADESH  ", "  mLOpS_ENGineer  ", "  LIAM,MAYA "]
sanitized_records = []

# Loop, clean, and save
for item in raw_survey_inputs:
    sanitized_records.append(item.strip().lower())

# Show the final results
print("Raw Inputs        :", raw_survey_inputs)
print("Sanitized Records :", sanitized_records)
Raw Inputs        : ['  ALICE SMITH ', ' dhaka, BANGLADESH  ', '  mLOpS_ENGineer  ', '  LIAM,MAYA ']
Sanitized Records : ['alice smith', 'dhaka, bangladesh', 'mlops_engineer', 'liam,maya']