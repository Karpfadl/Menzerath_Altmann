import re

import cmudict

from main.lang_specific.LangInterface import LangInterface


class EnglishHandler(LangInterface):
    def __init__(self):
        self.dictionary = cmudict.dict()

    def word_split(self, text_: str):
        return text_.split(" ")

    def count_syllables(self, word_):
        lengths = [len(list(y for y in x if y[-1].isdigit())) for x in self.dictionary[word_.lower()]]
        if lengths and (length := lengths[0]) > 0:
            return length
        else:
            return 2  # TODO find cleaner way to calculate
