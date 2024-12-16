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
    """
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    e_count = 0
    f_count = 0
    g_count = 0
    h_count = 0
    i_count = 0
    j_count = 0
    k_count = 0
    l_count = 0
    m_count = 0
    n_count = 0
    o_count = 0
    p_count = 0
    q_count = 0
    r_count = 0
    s_count = 0
    t_count = 0
    u_count = 0
    v_count = 0
    w_count = 0
    x_count = 0
    y_count = 0
    z_count = 0
    
    for i in text:
        if i == "a":
            a_count += 1
        elif i == "b":
            b_count += 1
        elif i == "c":
            c_count += 1
        elif i == "d":
            d_count += 1
        elif i == "e":
            e_count += 1
        elif i == "f":
            f_count += 1
        elif i == "g":
            g_count += 1
        elif i == "h":
            h_count += 1
        elif i == "i":
            i_count += 1
        elif i == "j":
            j_count += 1
        elif i == "k":
            k_count += 1
        elif i == "l":
            l_count += 1
        elif i == "m":
            m_count += 1
        elif i == "n":
            n_count += 1
        elif i == "o":
            o_count += 1
        elif i == "p":
            p_count += 1
        elif i == "q":
            q_count += 1
        elif i == "r":
            r_count += 1
        elif i == "s":
            s_count += 1
        elif i == "t":
            t_count += 1
        elif i == "u":
            u_count += 1
        elif i == "v":
            v_count += 1
        elif i == "w":
            w_count += 1
        elif i == "x":
            x_count += 1
        elif i == "y":
            y_count += 1
        elif i == "z":
            z_count += 1

    print("A count:", a_count)
    """

main()
