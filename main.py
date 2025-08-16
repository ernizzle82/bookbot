from stats import get_num_words, chars_dict_to_sorted_list, get_chars_dict

def get_book_text(path_to_file: str) -> str:
    with open(path_to_file, "r", encoding="utf-8") as file:
        file_contents = file.read()

    return file_contents


def main():
    path_to_file = "books/frankenstein.txt"

    file_contents = get_book_text(path_to_file)

    character_counts = get_chars_dict(file_contents)

    sorted_dicts = chars_dict_to_sorted_list(character_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(file_contents)} total words")
    print("--------- Character Count -------")
    for item in sorted_dicts:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
