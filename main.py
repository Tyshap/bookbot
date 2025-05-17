from stats import count_words, count_characters, sorted_characters
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        num_words = count_words(get_book_text(sys.argv[1]))
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        character_list = sorted_characters(count_characters(get_book_text(sys.argv[1])))
        for n in character_list:
            if n["name"].isalpha():
                print(f"{n["name"]}: {n["num"]}")
        print("============= END ===============")


main()