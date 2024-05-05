import tkinter as tk
from tkinter import filedialog

from describe_project import do_describe_folder


def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        print("Selected folder:", folder_path)
        result_set = do_describe_folder(folder_path)
        for k in result_set.keys():
            text.insert(tk.END, f"File: \n{k} ---> Description:\n {result_set.get(k)}")
            text.insert(tk.END, "\n\n\n")


root = tk.Tk()
root.title("Describe A Python Project")

# set fullscreen window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

select_folder_button = tk.Button(root, text="Select The Folder You Want To Describe", command=select_folder)
select_folder_button.pack()

text = tk.Text(root, wrap=tk.WORD)
text.pack(fill='both')


root.mainloop()
