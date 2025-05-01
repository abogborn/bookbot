import sys
from stats import get_num_words, count_letters, sort_count

def main ():

    # sys.argv handling

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Count number of words in frankenstein.txt

    #path = "books/frankenstein.txt"
    num_words = get_num_words(get_book_text(sys.argv[1]))
    #print(f"{num_words} words found in the document")

    # Count individual letters in frankenstein.txt

    count_dictionary = count_letters(get_book_text(sys.argv[1]))
    #print(count_dictionary)

    # Generate dictionary of characters and count, sort from high to low, then process into a report

    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for key in sort_count(count_dictionary):
        if (key["char"]).isalpha() == True:
            print(f"{key['char']}: {str(key['num'])}")

    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

main()