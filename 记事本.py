import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import re
import os

def update_word_count(*args):
    text = text_box.get("1.0", tk.END)
    pattern = re.compile(r'[\u4e00-\u9fa5]|[~！@#￥%……&*（）——+{}|：“”《》？·\-=\[\]、；‘，。/!$^()_{}|:"<>?`\\\;\',.]|\d+|\b\w+\b')
    word_count = len(re.findall(pattern, text))
    word_count_label.config(text=f"字数: {word_count}")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("文本文件", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, text)
        file_label.config(text=f"文件: {os.path.basename(file_path)}")
        update_word_count()

def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=[("文本文件", "*.txt")], defaultextension=".txt")
    if file_path:
        text = text_box.get("1.0", tk.END)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
        file_label.config(text=f"文件: {os.path.basename(file_path)}")

root = tk.Tk()
root.title("字数统计")

style = ttk.Style()
style.theme_use('clam')

open_button = ttk.Button(root, text="打开", command=open_file)
open_button.grid(row=0, column=0, padx=10, pady=10)

save_button = ttk.Button(root, text="保存", command=save_file)
save_button.grid(row=0, column=1, padx=10, pady=10)

text_frame = ttk.Frame(root)
text_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

text_box = tk.Text(text_frame, width=80, height=20)
text_box.pack(side=tk.LEFT)

scrollbar = ttk.Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

scrollbar.config(command=text_box.yview)
text_box.config(yscrollcommand=scrollbar.set)

word_count_label = ttk.Label(root, text="字数: 0")
word_count_label.grid(row=2, column=0, columnspan=2, pady=10)

file_label = ttk.Label(root, text="文件: ")
file_label.grid(row=3, column=0, columnspan=2, pady=10)

text_box.bind("<KeyRelease>", update_word_count)

root.mainloop()