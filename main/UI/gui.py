import tkinter as tk
from pathlib import Path
import pandas as pd
from main.constructs import TextProcessing
from main.constructs.Processor import Processor
from main.lang_specific.LangRegister import lang_register
from tkinter import filedialog

from main.workflow import MACalculator

root = tk.Tk()
root.geometry("300x300")
root.title("MA calc")

mail = tk.Label(root, text="volker.groeller@gmail.com", font=("Arial", 8)).grid(row=10)

#input boxes
fields = dict()

def get_input_folder():
    fields["input_folder"] = filedialog.askdirectory()

def get_output_folder():
    fields["output_folder"] = filedialog.askdirectory()


tk.Button(text='Input Folder', command=get_input_folder).grid(row=0)
tk.Button(text='Output Folder', command=get_output_folder).grid(row=1)

"""e1 = tk.Entry(root, width=80)
e2 = tk.Entry(root, width=80)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)"""

#language
def get_lang(selection):
    fields["language"] = selection


available_langs = lang_register.keys()
options = tk.StringVar(root, "language")
tk.OptionMenu(root, options, *available_langs, command=get_lang).grid(row=2)

#running the analysis
def run_calc():
    for file in Path(fields["input_folder"]).iterdir():
        text = TextProcessing.get_text(file.absolute())
        processor = Processor(fields["language"])
        result = MACalculator.calculate_ma(processor, text)
        df = pd.DataFrame(data=result, columns=["length", "avg. length", "freq"])
        out_path = Path(fields["output_folder"]) / Path(file.stem + ".csv")
        df.to_csv(out_path, sep=";", index=False)


tk.Button(text='run', command=run_calc).grid(row=4)


root.mainloop()


