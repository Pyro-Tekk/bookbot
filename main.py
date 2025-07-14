# main.py
count = 0

from stats import get_num_words
from stats import get_num_letters

    
    
def main():
    get_num_words("books/frankenstein.txt")
    
    get_num_letters("books/frankenstein.txt")
    

main()  # This runs your program!