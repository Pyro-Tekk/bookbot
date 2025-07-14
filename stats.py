
def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        split = file_contents.split()
        print(f"{len(split)} words found in the document")
    
    return


    