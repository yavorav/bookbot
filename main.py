# 
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #characters = count_characters(file_contents.lower())
        
        words = count_words(file_contents)
        return words

def count_words(text):
    count = len(text.split())
    return count

def count_characters(text):
    alphabet = []
    letter_count = int
    for i in alphabet:
        for j in text:
            if j == i:
                letter_count += 1   # this loops through the book 26 times... wouldn't it be better to loop once and just compare the letters?

print("Word Count:", main())
