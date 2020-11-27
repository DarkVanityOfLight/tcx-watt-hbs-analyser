#!/usr/bin/python3

# Imports
from parser import PlotPage, parse_file
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
# Variable declarations
root = tk.Tk()

# Classes
class LoadFilesPage(ttk.Frame):
    plot = Figure()

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        load_button = ttk.Button(self, text="Load File",command=self.load_file)
        load_button.pack()
        files_label = ttk.Label(self, text="Files loaded:")
        files_label.pack()


    def load_file(self):
       filename = filedialog.askopenfilename(
               initialdir="/", 
               title="Select file to load", 
               filetypes=(("xml files", ".xml"), ("training files", "*.tcx"), ("all files", "*.*"))) 
       hbs, watts, ffit = parse_file(filename)
       label = ttk.Label(self, text=filename)
       label.pack()
    

# Functions

# Main

if __name__ == "__main__":
    root.geometry("500x200")
    load_files_page = LoadFilesPage(root)
    load_files_page.pack()
    root.mainloop()
    
