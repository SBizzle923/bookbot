from stats import word_count, char_count

def get_book_text(filepath):
    contents = ""

    with open(filepath) as f:
        contents = f.read()

    return contents

def main():
    c = get_book_text("books/frankenstein.txt")

    count = word_count(c)
    print(f"{count} words found in the document")

    characters = char_count(c)
    print(characters)

main()