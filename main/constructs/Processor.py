from main.lang_specific.LangRegister import lang_register


class Processor:
    def __init__(self, lang: str):  # TODO error handling
        lang_specific_processor = lang_register[lang]()
        self.split_into_words = lang_specific_processor.word_split
        self.count_syllables = lang_specific_processor.count_syllables
