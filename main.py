import sys
# Import count functions
from stats import get_num_words, count_frequencies, get_sorted_frequencies

def main():
    # Check if a filename was provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filename = sys.argv[1]
    
    # Read the book file
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Error: Could not decode '{filename}' with UTF-8. Try a different encoding.")
        sys.exit(1)
    
    print('============ BOOKBOT ============')
    print(f"Analyzing book found at {filename}...")
    
    print("----------- Word Count ----------")
    word_count = get_num_words(text)
    print(f"Found {word_count} total words")
    
    # Count characters
    freq = count_frequencies(text)
    print("--------- Character Count -------")
    # Sort counted characters (alphabetic only)
    sorted_chars = get_sorted_frequencies(freq)
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()