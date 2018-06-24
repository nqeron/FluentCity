from collections import namedtuple
import string
import math

Letter_Distribution = namedtuple("LetterDistribution", list(string.ascii_lowercase))  # this named tuple structure
# gives a slot to count all the letters from a-z in a given word, providing a hashable object

PHI = (1 + math.sqrt(5))/2


def get_letter_counts(word):
    """

    This method returns a unique letter count tuple for the provided word
    :param word: word to count the letters in
    :return: _Letter_Distribution tuple
    """
    word = word.lower()  # translate word to only lowercase letters
    counts_list = [0] * 26
    for i in word:
        counts_list[string.ascii_lowercase.index(i)] +=1
    return Letter_Distribution(*counts_list)


def search_for_word_in_dict(search_word, path_to_dict):
    """

    This method searches a given dictionary for a given word and returns all of the valid anagrams
    :param search_word: This is the word to search the dictionary for
    :param path_to_dict: This is the file path of the dictionary to search
    :return: returns None if the word is not found in the dictionary otherwise it returns all anagrams found
    """
    anagram_dictionary = {}  # initialize the dictionary to put the anagrams into
    search_word = search_word.lower()  # translate the search word to lowercase
    if not search_word:  # if there is no search word, then it by definition isn't in the dictionary - no need to search
        return None
    with open(path_to_dict) as dict_in:  # open the dictionary file provided inside a context manager
        for word in dict_in: # for every line ( parsed by \n s) in the dictionary file, grab the word
            word = word.strip()  # get rid of trailing \n character
            letter_set = get_letter_counts(word)  # Here's where things get a bit clever - each word is gets its letters
            # counted and put into a tuple - a hashable object, this means that all words that are anagrams of each
            # other will share this same tuple and therefore hash address
            # so the word is added to the anagram dictionary alongside it's fellow anagrams!
            if letter_set not in anagram_dictionary:  # checks to see whether this count is already in the dictionary
                anagram_dictionary[letter_set] = [word]  # if not, instantiates it
            else:
                anagram_dictionary[letter_set].append(word)  # otherwise, it appends the word to the pre-existing list
    letter_set = get_letter_counts(search_word)  # gets the letter count for the word
    if letter_set not in anagram_dictionary:  # if the letter count isn't in the dictionary, then neither is the word!
        return None
    anagrams = anagram_dictionary[letter_set]  # gets the full list of words
    if search_word not in anagrams:  # check that the word was actually added from the dictionary
        return None
    anagrams.remove(search_word)  # remove the search word from potential anagrams
    anagrams.sort(key=lambda w: w[1])  # sort by second letter!
    return anagrams


def fib(n):
    """
    A silly little function to approximate the nth fibonacci number
    :param n:
    :return: the nth fibonacci number
    """
    return math.floor(math.pow(PHI, n)/ math.sqrt(5))