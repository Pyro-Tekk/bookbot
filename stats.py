def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        split = file_contents.split()
        print(f"{len(split)} words found in the document")
    
    return


letters = {}

def get_num_letters(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        all_lower = file_contents.lower()
        characters = list(all_lower)

    

    for character in characters:
        if character in letters:
            letters[character] += 1
        else:
            letters[character] = 1

     
    print(letters)
               
        #print(f"{len(split)} words found in the document")
    
    return




  

    