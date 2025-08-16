def get_num_words(text: str) -> int:
    word_list = text.split()
    return len(word_list)


def get_chars_dict(text: str) -> dict:
    # create dictionary to store letter counts
    char_count = dict()

    for char in text.lower():
        # check if char exists, if not create and set to 1, otherwise increase
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


def sort_on_num_key(items: dict) -> int:
    return items["num"]

def chars_dict_to_sorted_list(dictionary: dict) -> list:
    # create empty list to hold dictionarie pairs
    list_of_dicts = list()

    # populate list of dicts
    for key in dictionary:
        current_dict = {"char": key, "num": dictionary[key]}
        list_of_dicts.append(current_dict)

    # sort list of dicts
    list_of_dicts.sort(key=sort_on_num_key, reverse=True)
    return list_of_dicts

