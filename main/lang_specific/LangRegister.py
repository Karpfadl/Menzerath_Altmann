from main.lang_specific.russian.russian import word_split, count_syllables

lang_register = dict(
    russian=(word_split, count_syllables)
)
