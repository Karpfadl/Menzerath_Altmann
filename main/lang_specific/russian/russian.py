import re
from main.lang_specific.LangInterface import LangInterface


class RussianHandler(LangInterface):

    def word_split(self, text_: str):
        return text_.split(" ")

    def count_syllables(self, word_):
        return len(re.findall(r"[аАэЭыЫоОуУяЯеЕиИёЁюЮ]", word_))
