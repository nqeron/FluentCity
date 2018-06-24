import unittest
import anagram_finder


class LetterDistributionTest(unittest.TestCase):
    def testNoWord(self):
        no_letters = [0] * 26
        self.assertEqual(anagram_finder.Letter_Distribution(*no_letters), anagram_finder.get_letter_counts(""))

    def testOneLetter(self):
        letters = [0] * 26
        letters[0] = 1
        self.assertEqual(anagram_finder.Letter_Distribution(*letters), anagram_finder.get_letter_counts("a"))

    def testNonRepeatingWord(self):
        letters = [0] * 26
        letters[9] = 1  # j
        letters[4] = 1  # e
        letters[13] = 1  # n
        letters[20] = 1  # u
        self.assertEqual(anagram_finder.Letter_Distribution(*letters), anagram_finder.get_letter_counts("june"))

    def testMixedCase(self):
        letters = [0] * 26
        letters[0] = 1  # a
        letters[11] = 1  # l
        letters[14] = 1  # o
        letters[15] = 1  # p
        self.assertEqual(anagram_finder.Letter_Distribution(*letters), anagram_finder.get_letter_counts("OpAl"))

    def testRepeatingWord(self):
        letters = [0] * 26
        letters[2] = 2  # c
        letters[4] = 1  # e
        letters[18] = 3  # s
        letters[20] = 1  # u
        self.assertEqual(anagram_finder.Letter_Distribution(*letters), anagram_finder.get_letter_counts("success"))

    def testContents(self):
        letters = [0] * 26
        letters[2] = 2
        letters[4] = 1
        letters[18] = 3
        letters[20] = 1
        distribution = anagram_finder.Letter_Distribution(*letters)
        self.assertEqual(0, distribution.a)
        self.assertEqual(1, distribution.e)
        self.assertEqual(3, distribution.s)


class DictionarySearchTest(unittest.TestCase):
    dict_path = "dict/dictionary.txt"

    def testMultipleAnagrams(self):
        self.assertEqual(['garel', 'garle', 'lager', 'large', 'geral', 'legra', 'elgar', 'glare', 'argel', 'argle',
                          'ergal'], anagram_finder.search_for_word_in_dict("regal", self.dict_path))

    def testNoAnagrams(self):
        self.assertEqual([], anagram_finder.search_for_word_in_dict("aaah", self.dict_path))

    def testWordDoesNotExist(self):
        self.assertEqual(None, anagram_finder.search_for_word_in_dict("qwzectl", self.dict_path))

    def testMixedCase(self):
        self.assertEqual(['rate', 'tare', 'reta', 'tera', 'aret', 'arte', 'erat', 'ater'],
                         anagram_finder.search_for_word_in_dict("TeAr", self.dict_path))

    def testNullString(self):
        self.assertEqual(None, anagram_finder.search_for_word_in_dict("", self.dict_path))


if __name__ == '__main__':
    unittest.main()
