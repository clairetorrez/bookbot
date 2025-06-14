import sys
from stats import get_num_words, get_num_chars, sort_char_counts

def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)

    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    sorted_list = sort_char_counts(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_list:
        char = item["char"]
        count = item["num"]
        print(f"{char}: {count}")

if __name__ == "__main__":
    main()