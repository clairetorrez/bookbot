def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_chars(text):
    text = text.lower()
    num_chars = {}

    for char in text:
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1

    return num_chars

def sort_char_counts(num_chars):
    sorted_list = []

    for char, count in num_chars.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})

    sorted_list.sort(key=lambda item: item["num"], reverse=True)
    return sorted_list
