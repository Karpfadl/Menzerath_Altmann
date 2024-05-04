from main.lang_specific.LangRegister import lang_register


class Processor:
    def __init__(self, lang: str):  # TODO error handling
        word_split_func, syllable_count_func = lang_register[lang]
        self.split_into_words = word_split_func
        self.count_syllables = syllable_count_func
