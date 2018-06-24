# Fluent City Anagram Searcher

## Introduction

This code is in response to a coding challenge posed by Fluent City in order to build a dictionary scraping anagram
finder.

The brunt of the logic is found in the **anagram_finder.py** file. The **run.py** file provides a way to actually run
the program and see the results in a console. Finally, the **tests.py** file contains the various unittests for the
program to ensure that edge cases are caught and that the code is functioning according to plan.

## Methodology

The program operates by creating a dictionary that hashes a given word's letter distribution counts and maps it to all
the other words with the same letter count. This enables a quick lookup to find all the anagrams and check for the
existence of a given word. The dictionary is built up by iterating over the file, using python's built-in iteration by
new-lines.

## Design comments

There are a few design pieces I'd like to comment on.

### Named tuples

I used a namedtuple in order to create the letter distribution counts. While an ordinary tuple could have done the job,
I wanted to ensure that there were 26 slots - one for each letter. The downside to this is that it takes up a bit more
space.

### Dictionary

I used a dictionary for my main lookup. Since the hashing process is effectively O(1), this is quite an efficient way
to find the anagrams for a given word. The downside comes with the potential size of the dictionary, which would easily
increase given a proportional increase in the number of words. Interestingly, the use of the letter count tuple hash will
reduce the size by a small bit.

### Running / Loading
The dictionary is loaded once per word operation. This means that in order to search for successive words, the dictionary
has to be re-loaded into memory for each one. This is quite inefficient. This could be addressed by loading the dictionary
in once at the beginning of all the searches, and keeping it in memory while each one is done successively.
