from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary.
    >>> words = WordFinder("/usr/share/dict/words")
    235886 words read

    """
   
    def __init__(self, path):
        """Makes a list of words from file in path
        and returns how many words it read"""
        self.words = open(path, 'r')
        self.words_list = self.make_word_list()
        print(self.count_words(self.words_list))

    def __repr__(self):
        return f"<WordFinder words_list={self.words_list}>"

    def make_word_list(self):
        """makes list of stripped words from file"""
        return [word.strip() for word in self.words.readlines()]

    def count_words(self, stripped_words):
        return f"{len(stripped_words)} words read"

    def random(self):
        return choice(self.words_list)
