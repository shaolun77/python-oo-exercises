"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:

"""Machine for finding random words from dictionary.
    
Create a class that is instantiated with a path to a file on disk that contains words, one word per line

it reads that file, and makes an attribute of a list of those words
it prints out “[num-of-words-read] words read”
(it doesnt need to do all of this directly in the __init__ method;
it might be a good idea for the __init__ method to call other functions to do some of this.)

it provides a method, random(), which returns a random word from that list of words

Note: the random method should not re-read the list of words each time; 
it should work with the already-read-in list of words.

For example, assume you have a file at /Users/student/words.txt that looks like this:
cat
dog
porcupine

Working with your class should work like this:
    
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, path):
        """Read dictionary and reports # items read."""

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file -> list of words.
        strip() removes spaces before and after the word"""

        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word."""

        return random.choice(self.words)


class SpecialWordFinder(WordFInder):

""" Make a subclass, SpecialWordFinder, that uses WordFinder, but changes needed parts so it can work. 
Try to do this so as little code as needed is duplicated.

    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

"""

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]