def count_words(file_contents):
    num_words = 0
    words = file_contents.split()
    for word in words:
        num_words += 1
    return num_words

def count_characters(file_contents):
    characters = {}
    file_contents = file_contents.lower()
    for letter in file_contents:
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1
    return characters

def sort_on(dict):
    return dict["num"]

def sorted_characters(character_dict):
    return_list = []
    for entry in character_dict:
        return_list.append({"name": entry, "num": character_dict[entry]})
    return_list.sort(reverse=True, key=sort_on)
    return return_list

    