from stats import count_characters, count_words


def get_book_text(path_to_file: str) -> str:
    with open(path_to_file, "r", encoding="utf-8") as file:
        file_contents = file.read()

    return file_contents


def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_book_text(path_to_file)

    print(f"{count_words(file_contents)} words found in the document")
    print(count_characters(file_contents))


if __name__ == "__main__":
    main()
