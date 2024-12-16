# 
def main():
    with open("books/frankenstein.txt") as f: # Opens the file
        file_contents = f.read() # reads the contents of the book and assigns it to the file_contents variable as a string
        words = count_words(file_contents) # calls the count_words function on the book, assigning the number of words to the words variable
        characters = count_characters(file_contents.lower()) # calls the count_characters function on the book, assigning the dictionary to the characters variable
        # Printing and formatting the report of the book
        print("*** Report of book: Frankenstein ***")
        print("Word Count:", words)
        for a in characters:
            print(f"The letter '{a}' occurs {characters[a[0]]} times.")
        print("*** End of Report ***")

# Function takes in a string of text and returns the number of words in the text
def count_words(text):
    count = len(text.split())
    return count # returns int

# Function takes in a string of text and returns a dictionary with the letters that occur in the text and the number of occurences of each letter
def count_characters(text):
    letters = {} # initializes the dictionary
    for i in text: # iterates through each character in the text
        if i.isalpha(): # checks that its a letter and not a special character or space
            if i in letters:
                letters[i] += 1 # if the letter is already a key in the dictionary, add to its value
            else:
                letters[i] = 1 # if the letter does not already have a key in the dictionary, add one setting it to 1 for this first occurence
            
    return letters # returns dictionary

main()
