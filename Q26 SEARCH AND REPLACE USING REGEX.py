import re

text = "Python is a popular programming language. Python is used for web development, data science, and more."
print("Original Text\n", text)
search_word = input("\nEnter the word to search: ")
replace_word = input("Enter the word to replace it with: ")
new_text = re.sub(search_word, replace_word, text)
print("\nUpdated Text:\n", new_text)
