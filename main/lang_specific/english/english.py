import re

import cmudict

from main.lang_specific.LangInterface import LangInterface


class EnglishHandler(LangInterface):
    def __init__(self):
        self.dictionary = cmudict.dict()

    def word_split(self, text_: str):
        return text_.split(" ")

    def count_syllables(self, word_):
        if (length := len(self.dictionary[word_.lower()])) > 0:
            return length
        else:
            return 2  # TODO find cleaner way to calculate
