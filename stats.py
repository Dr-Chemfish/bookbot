import sys

def get_num_words():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    num_words = len(file_contents.split())
    print(f"Found {num_words} total words")


def get_num_characters():
    character_list = {}
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    words = file_contents.split()
    for word in words:
        word = word.lower()
        for character in word:
            if (character in character_list) == False:
                character_list[character] = 1
            else:
                character_list[character] += 1
    return character_list

def convert_dict_to_list_of_dict(dict):
    char_list =[]
    for char in dict:
        char_dict = {}
        char_dict["char"]=char
        char_dict["num"]=dict[char]
        char_list.append(char_dict)
    return char_list

def sort_on(items):
    return items["num"]

def character_report(char_list):
    char_list = char_list
    char_list.sort(reverse=True, key=sort_on)
    for set in char_list:
        if set["char"].isalpha():
            print(f"{set["char"]}: {set["num"]}")

def print_report():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    get_num_words()
    print("--------- Character Count -------")
    character_report(convert_dict_to_list_of_dict(get_num_characters()))
    print("============= END ===============")