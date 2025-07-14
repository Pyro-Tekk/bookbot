# main.py
count = 0

def get_word_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        split = file_contents.split()
        print(f"{len(split)} words found in the document")
    
    return 
    
    
def main():
    get_word_count("books/frankenstein.txt")
    

main()  # This runs your program!