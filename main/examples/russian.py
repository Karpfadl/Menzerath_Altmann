import time

from main.constructs import TextProcessing
from main.constructs.Processor import Processor
from main.workflow.MACalculator import calculate_ma

path = "C:/Program Files/PuTTY/README.txt"
lang = "english"

text = TextProcessing.get_text(path)

processor = Processor(lang)
start = time.time()
wol = calculate_ma(processor, text)
end = time.time()
print(f"time: {end - start}")
print(wol)
