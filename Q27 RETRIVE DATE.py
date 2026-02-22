import re

text = input("Enter a string containing a date: ")

pattern = r'\b(?:\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}|\d{4}[-/.]\d{1,2}[-/.]\d{1,2})\b'

match = re.findall(pattern, text)

if match:
    print("Date(s) found:", match)
else:
    print("No date found")
