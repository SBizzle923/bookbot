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

def sort_by_count(dict):
    list = []

    for key in dict:
        list.append({"char": key, "num": dict[key]})    

    list.sort(reverse=True, key=sort_count)
    return list

def sort_count(dict):
    return dict["num"]