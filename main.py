# main.py

import sys
from stats import get_num_words
from stats import get_num_letters
from stats import sort_characters_by_count

if len(sys.argv) != 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)    
    
def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    get_num_words(sys.argv[1])
    print("--------- Character Count -------")    
    letters_dict = get_num_letters(sys.argv[1])
    sorted_chars = sort_characters_by_count(letters_dict)
    for char_info in sorted_chars:
        if char_info["char"].isalpha():
            print(f"{char_info['char']}: {char_info['num']}")
    print("============= END ===============")

main()  # This runs your program!