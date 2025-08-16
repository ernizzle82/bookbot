def get_book_text(path_to_file: str) -> str:
    with open(path_to_file, "r", encoding="utf-8") as file:
        file_contents = file.read()

    return file_contents


def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_book_text(path_to_file)

    print(file_contents)


if __name__ == "__main__":
    main()
