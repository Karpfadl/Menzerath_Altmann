import numpy as np

from main.constructs.Processor import Processor


def calculate_ma(processor: Processor, text):
    result_dict = dict()
    for word in processor.split_into_words(text):
        syllable_count = processor.count_syllables(word)  # speed up by remembering words already processed
        if syllable_count == 0:
            continue
        if syllable_count in result_dict:
            result_dict[syllable_count].append(len(word) / float(syllable_count))
        else:
            result_dict[syllable_count] = [len(word) / float(syllable_count)]
    return [(rank[0], np.sum(rank[1]) / len(rank[1]), len(rank[1])) for rank in sorted(result_dict.items())]
