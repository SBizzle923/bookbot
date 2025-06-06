def word_count(content):
    words = content.split()
    return len(words)

def char_count(content):
    seen_chars = set()
    chars = {}

    for char in content:
        c = char.lower()
        if c in seen_chars:
            chars[c] += 1
        else:
            seen_chars.add(c)
            chars[c] = 1

    return chars