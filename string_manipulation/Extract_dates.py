# Extract Dates
# The Date should follow the format DD-MM-YYYY

import re

text = "Today's date is 28-04-2025 and tomorrow date is 29-04-2025..."
# pattern = r"\b\d{2}-\d{2}-\d{4}\b"
pattern = r"\d{2}-\d{2}-\d{4}"
extracted_date = re.findall(pattern, text)
print(extracted_date)