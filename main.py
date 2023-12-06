def main():
    book_path = "books/frankenstein.txt"
    #text = get_book_text(book_path)
    #print(text)
    #print(count_words(text))
    #print(count_letters(text))
    book_report(book_path)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(book):
    list_of_words = book.split()
    num_of_words = len(list_of_words)
    return num_of_words

def count_letters(text):
    alphabet = {}
    for l in text:
            a = l.lower()
            if a in alphabet:
                alphabet[a] += 1
            else:
                alphabet[a] = 1
    return alphabet

def book_report(book_path):
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_dict = count_letters(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} found in the document")
    print()
    for char in char_dict:
        if char.isalpha():
            print(f"The {char} character was found {char_dict[char]} times")
    print("--- End report ---")

main()