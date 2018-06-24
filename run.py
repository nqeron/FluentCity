import anagram_finder

DICTIONARY_PATH = "dict/dictionary.txt"


def print_header():
    print("-----------------------------")
    print("   Anagram Searcher App")
    print("-----------------------------")
    print()


def main():
    print_header()
    word = get_word()
    if not word:  # If there is no word, then
        return  # end the program
    anagram_finder.search_for_word_in_dict(word,DICTIONARY_PATH)


def get_word():
    word = ""
    while not word:
        word = input("Please enter in a word to search for : ")  # prompt the user for input
        word = word.strip()  # remove any trailing spaces
        if not word:  # if there is no word entered
            return ""  # stop the whole search loop
        if len(word.split()) > 1:  # ensure that there is indeed only one word
            print("Please enter only a single word!")
            continue
    return word


if __name__ == '__main__':  # ensure that this can be used as part of other packages without running code
    main()