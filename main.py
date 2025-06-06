from stats import word_count, char_count, sort_by_count

def get_book_text(filepath):
    contents = ""

    with open(filepath) as f:
        contents = f.read()

    return contents

def main():
    c = get_book_text("books/frankenstein.txt")

    count = word_count(c)
    print(f"Found {count} total words")

    characters = char_count(c)

    sorted_characters = sort_by_count(characters)

    for char in sorted_characters:
        if char["char"].isalpha() is True:
            print(f"{char["char"]}: {char["num"]}")

main()