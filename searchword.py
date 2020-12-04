import json

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    else:
        return "The word does not exist. Please double check the word, and try again."

word = input("Enter word: ")

print(translate(word))

