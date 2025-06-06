def get_book_text(filepath):
    contents = ""

    with open(filepath) as f:
        contents = f.read()

    return contents

def word_count(content):
    words = content.split()
    return len(words)

def main():
    c = get_book_text("books/frankenstein.txt")
    count = word_count(c)
    print(f"{count} words found in the document")

main()
