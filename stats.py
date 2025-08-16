def count_words(text: str) -> int:
    word_list = text.split()
    return len(word_list)


def count_characters(text: str) -> dict:
    # create dictionary to store letter counts
    char_count = dict()

    for char in text.lower():
        # check if char exists, if not create and set to 1, otherwise increase
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count
