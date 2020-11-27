#!/usr/bin/python3

# Imports
import tkinter as tk
from tkinter import ttk
# Variable declarations
root = tk.Tk()

# Classes
class LoadFilesPage(ttk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent


# Functions

# Main

if __name__ == "__main__":
    root.geometry("500x200")
    load_files_page = LoadFilesPage(root)
    load_files_page.pack()
    root.mainloop()
    
