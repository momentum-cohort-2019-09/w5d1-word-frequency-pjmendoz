import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def clean_word(word):
    # Given one string: 

        # - clean the string (remove punctuation from the beginning and end of the string)
        # , normalize it (lowercase, remove possessives) 
    
    # and return the string. 

    word = word.strip(string.punctuation)
    word = word.lower()
    if word[-2:] === "'s":
        word = word[:-2]

    return word

def clean_words(words):
    cleaned_words = []
    for word in words: 
        cleaned_words.append(clean_word(word))
    return cleaned_words    

def print_word_freq(filename):
    #read the file
    with open(filename) as file: 
        text = file.read()

    #split the file in words
    words = text.split()

    #clean each word
    words = clean_words(words)

    #remove stop words
    #calculate the frequency of each word --- needs a dictionary     