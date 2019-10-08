STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):

    with open(file) as my_hw: 
         my_hw = my_hw.read().lower()

         my_hw = my_hw.split()

         my_words =[]

         for word in my_hw:
             word = word.lower()

             my_words.append(word)

         def clean_text(text):

            all_letters = "abcdefghijklmnopqrstuvwxyz"
            keep_text = ""
            for char in text:
                if char in all_letters:
                    keep_text += char
            return keep_text

         clean_words =[]

         for word in my_words:
            clean_words.append(clean_text(word))

         print(clean_words)    



#remove stop words
#calculate the frequency of each word -- needs a dictionary
#utilize .count to put each word in a dictionary


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
