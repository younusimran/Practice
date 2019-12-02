# count characters in text file and copy it new text file, sorted and unsorted based on number of counts

import tkinter as tk
from tkinter import filedialog
import re
import os
from os import strerror

root = tk.Tk()
root.withdraw()

file_name = filedialog.askopenfilename(title = "select file to open", filetypes = [("Text file", "*.txt")])
ch_dict = {}
cnt = 0
try:
    with open(file_name) as f:
        data = f.read()
        for ch in data:
            if not re.match('[a-zA-z]', ch):
                continue
            else:
                if ch in ch_dict.keys():
                    ch_dict[ch] = ch_dict[ch] + 1
                else:
                    ch_dict[ch] = 1

    f_save = os.path.basename(file_name).split(".")
    file_save = os.path.join(os.path.dirname(file_name),f_save[0]+".hist.txt")
    with open(file_save, 'w') as w:
        w.write("-------Unsorted count-------\n")
        for k,v in ch_dict.items():
            w.write(k+" -> "+str(v)+'\n')
        w.write("\n\n")
        w.write("-------Sorted based on count-------\n")
        for k,v in sorted(ch_dict.items(), key = lambda x:(x[1],x[0]), reverse = True):
            w.write(k+" -> "+str(v)+'\n')
except Exception as e:
    print(strerror(e.errno))