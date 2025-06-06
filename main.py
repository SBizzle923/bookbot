import sys
from stats import word_count, char_count, sort_by_count

def get_book_text(filepath):
    contents = ""

    with open(filepath) as f:
        contents = f.read()

    return contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    c = get_book_text(sys.argv[1])

    count = word_count(c)
    print(f"Found {count} total words")

    characters = char_count(c)

    sorted_characters = sort_by_count(characters)

    for char in sorted_characters:
        if char["char"].isalpha() is True:
            print(f"{char["char"]}: {char["num"]}")

main()