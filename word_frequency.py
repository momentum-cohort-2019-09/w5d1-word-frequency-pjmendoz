STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as my_hw: 
         my_hw = my_hw.read().lower()

         my_hw = my_hw.split()

         print(my_hw)

    def clean_text(text):
        all_letters = "abcdefghijklmnopqrstuvwxyz"
        text_to_keep = ""
        for char in text: 
            if char in all_letters: 
                text_to_keep += char
        return text_to_keep    


# print_word_freq(seneca_falls.txt)

# print(print_word_freq)

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
