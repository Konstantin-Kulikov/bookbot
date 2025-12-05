import sys
from stats import count_words, count_characters, sort_dictionaries

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents


book_text = get_book_text(book_path)
characters_d = count_characters(book_text)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
count_words(book_text)
print("--------- Character Count -------")

result = sort_dictionaries(characters_d)
for i in result:
    if i['char'].isalpha():
        print(f"{i['char']}: {i['num']}")


print("============= END ===============")