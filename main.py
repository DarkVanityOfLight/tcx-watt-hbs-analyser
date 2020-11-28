#!/usr/bin/python3

# Imports
from parser import PlotPage, parse_file
import tkinter as tk
from tkinter import ttk
from pathlib import Path
from tkinter import filedialog
from matplotlib.figure import Figure
# Variable declarations
root = tk.Tk(className=" Training Analyzer")

# Classes
class LoadFilesPage(ttk.Frame):
    figure = Figure()
    sub_plots = {}

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        load_button = ttk.Button(self, text="Load File",command=self.load_file)
        load_button.pack()
        display_button = ttk.Button(self, text="Display", command=self.plot_show)
        display_button.pack()
        files_label = ttk.Label(self, text="Files loaded:")
        files_label.pack()
        self.files = tk.Listbox(self, selectmode="MULTIPLE")
        self.files.pack()
        remove_button = ttk.Button(self, text="Remove selected", command=self.remove)
        remove_button.pack()

        self.ax = self.figure.add_subplot(1, 1, 1)

    def load_file(self):
       filename = filedialog.askopenfilename(
               initialdir=Path.home(), 
               title="Select file to load", 
               filetypes=(("xml files", ".xml"), ("training files", "*.tcx"), ("all files", "*.*"))) 
       hbs, watts, ffit, training_id = parse_file(filename)
       self.add_plot(hbs, watts, ffit, training_id)
    
    def add_plot(self, hbs, watts, ffit, training_id):
        plot, = self.ax.plot(hbs, ffit(hbs) ,label=training_id) 
        self.sub_plots[training_id] = plot
        self.files.insert(0, training_id)

    def plot_show(self):
        
        self.ax.legend(loc="best")
        plot_page = PlotPage(self.parent, self.figure)
        self.pack_forget()
        plot_page.pack()

    def remove(self):
        to_remove = self.files.curselection()
        
        for training in to_remove:
            training_id = self.files.get(training)
            self.files.delete(training)
            plot = self.sub_plots[training_id]
            plot.remove()

# Functions

# Main

if __name__ == "__main__":
    root.geometry("500x300")
    load_files_page = LoadFilesPage(root)
    load_files_page.pack()
    root.mainloop()
    
