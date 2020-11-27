#!/usr/bin/python3

# Imports
from parser import PlotPage, parse_file
import tkinter as tk
from tkinter import ttk
from pathlib import Path
from tkinter import filedialog
from matplotlib.figure import Figure
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
        display_button = ttk.Button(self, text="Display", command=self.plot_show)
        display_button.pack()
        files_label = ttk.Label(self, text="Files loaded:")
        files_label.pack()

        self.ax = self.plot.add_subplot(1, 1, 1)

    def load_file(self):
       filename = filedialog.askopenfilename(
               initialdir=Path.home(), 
               title="Select file to load", 
               filetypes=(("xml files", ".xml"), ("training files", "*.tcx"), ("all files", "*.*"))) 
       hbs, watts, ffit = parse_file(filename)
       self.add_plot(hbs, watts, ffit)
       label = ttk.Label(self, text=filename)
       label.pack()
    
    def add_plot(self, hbs, watts, ffit):
        self.ax.plot(hbs, watts, 'o', hbs, ffit(hbs)) 

    def plot_show(self):
        plot_page = PlotPage(self.parent, self.plot)
        self.pack_forget()
        plot_page.pack()

# Functions

# Main

if __name__ == "__main__":
    root.geometry("500x200")
    load_files_page = LoadFilesPage(root)
    load_files_page.pack()
    root.mainloop()
    
