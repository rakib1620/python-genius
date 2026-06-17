# --- LAB 4: THE PROFILE TEXT NORMALIZATION PIPELINE ---

# Raw messy user inputs from the survey form
raw_survey_inputs = ["  ALICE SMITH ", " dhaka, BANGLADESH  ", "  mLOpS_ENGineer  ", "  LIAM,MAYA "]

# Empty list container to store production-ready data
sanitized_records = []

# Loop through each individual string element inside the raw list
for item in raw_survey_inputs:
    # Remove leading/trailing whitespaces with .strip() and enforce lowercase with .lower()
    cleaned_text = item.strip().lower()
    
    # Append the normalized string dynamically into the sanitized container
    sanitized_records.append(cleaned_text)

# Print both lists to the terminal to visually audit the transformations
print("Raw Inputs        :", raw_survey_inputs)
print("Sanitized Records :", sanitized_records)