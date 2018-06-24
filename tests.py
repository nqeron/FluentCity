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

    def nonrepeatingWord(self):
        letters = [0] * 26
        letters[9] = 1  # j
        letters[4] = 1  # e
        letters[13] = 1  # n
        letters[20] = 1  # u
        self.assertEqual(anagram_finder.Letter_Distribution(*letters), anagram_finder.get_letter_counts("june"))

    def mixedCase(self):
        letters = [0] * 26
        letters[0] = 1  # a
        letters[11] = 1  # l
        letters[14] = 1  # o
        letters[15] = 1  # p
        self.assertEqual(anagram_finder.Letter_Distribution(*letters), anagram_finder.get_letter_counts("OpAl"))

    def repeatingWord(self):
        letters = [0] * 26
        letters[2] = 2  # c
        letters[4] = 1  # e
        letters[18] = 3  # s
        letters[20] = 1  # u
        self.assertEqual(anagram_finder.Letter_Distribution(*letters), anagram_finder.get_letter_counts("success"))


if __name__ == '__main__':
    unittest.main()