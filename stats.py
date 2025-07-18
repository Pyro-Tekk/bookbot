def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        split = file_contents.split()
        
    print(f"Found {len(split)} total words")
    
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
           
          
    return letters

def sort_characters_by_count(letters):
    def sort_on(items):
        return items["num"]
    
    new_dict_list = []
    for character, count in letters.items():
        char_dict = {"char": character, "num": count}
        new_dict_list.append(char_dict)

    new_dict_list.sort(reverse=True, key=sort_on)
    return new_dict_list
  

    