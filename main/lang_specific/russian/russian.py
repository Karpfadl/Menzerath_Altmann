import re


def word_split(text_: str):
    return text_.split(" ")


def count_syllables(word_):
    return len(re.findall(r"[аАэЭыЫоОуУяЯеЕиИёЁюЮ]", word_))
