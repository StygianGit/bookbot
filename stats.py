def count_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def count_characters(book_text):
    character_dictionary = {}
    characters = list(book_text.lower())
    for c in characters:
        if c in character_dictionary:
            character_dictionary[c] = character_dictionary[c] + 1
        if c not in character_dictionary:
            character_dictionary[c] = 1
    return character_dictionary

def sort_on_num(dictionary):
    return dictionary["num"]

def sort_dictionaries(dictionary):
    sorted_dict_list = []
    for k in dictionary:
        sorted_dictionary = {"char": k, "num": dictionary[k]}
        sorted_dict_list.append(sorted_dictionary)
    sorted_dict_list.sort(reverse=True, key=sort_on_num)
    return sorted_dict_list
    

    
        












        
            