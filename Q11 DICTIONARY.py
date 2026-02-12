dictionary = {
    "pen": "A tool used for writing",
    "car": "A vehicle with four wheels",
    "apple": "A juicy red fruit"
}

word = input("Enter a word: ").lower()
if word in dictionary:
    print("Meaning:", dictionary[word])
else:
    print("Word not found")
