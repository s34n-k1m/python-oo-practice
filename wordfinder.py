from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary.
    >>> words = WordFinder("/usr/share/dict/words")
    235886 words read

    """

    def __init__(self, path):
        """Makes a list of words from file in path
        and returns how many words it read"""
        file_contents = open(path)
        self.words = self.make_words(file_contents)
        print(len(self.words), "words read")

    def __repr__(self):
        return f"<{type(self)} words={self.words}>"

    def make_words(self, file_contents):
        """makes list of stripped words from file"""
        return [word.strip() for word in file_contents]

    def count_words(self, stripped_words):
        """Returns count of words from file"""
        return f"{len(stripped_words)} words read"

    def random(self):
        """Returns a random word from the list of words"""
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """SpecialWordFinder: ignores line comments and
    blank lines from file."""

    def make_words(self, file_contents):
        """Returns a list of words with blank lines and
        comment lines filtered out

        >>> special_words = SpecialWordFinder("specialwords.txt")
        4 words read
        """

        return [word.strip() for word in file_contents
                if word.strip() and not word.startswith("#")]
