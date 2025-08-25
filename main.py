import sys
from stats import get_num_words
from stats import get_num_characters
from stats import print_report

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print_report()

main()

