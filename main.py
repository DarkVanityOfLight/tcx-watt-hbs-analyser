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

    def __init__(self, parent, figure = None, sub_plots = None):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        top_button_container = ttk.Frame(self)
        top_button_container.pack(side=tk.TOP)

        list_container = ttk.Frame(self)
        list_container.pack()

        sub_list_container = ttk.Frame(list_container)
        sub_list_container.pack(side=tk.TOP, fill=tk.X)

        remove_button_container = ttk.Frame(list_container)
        remove_button_container.pack(side=tk.RIGHT, fill=tk.BOTH)

        load_button = ttk.Button(top_button_container, text="Load File",command=self.load_file)
        load_button.pack(side=tk.LEFT)
        display_button = ttk.Button(top_button_container, text="Display", command=self.plot_show)
        display_button.pack(side=tk.LEFT)
        files_label = ttk.Label(sub_list_container, text="Files loaded:")
        files_label.pack(side=tk.LEFT)
        self.files = tk.Listbox(list_container, selectmode="MULTIPLE")
        self.files.pack(side=tk.LEFT)
        remove_button = ttk.Button(remove_button_container, text="Remove selected", command=self.remove)
        remove_button.pack(side=tk.TOP)


        if figure != None and sub_plots != None:
            self.back_init(figure, sub_plots)
            self.ax = self.figure.axes[0]
        else:
            self.ax = self.figure.add_subplot(1, 1, 1)

    def back_init(self, figure, sub_plots):

        self.sub_plots = sub_plots
        self.figure = figure

        for plot in sub_plots.keys():
            self.files.insert(0, plot)


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
        plot_page = PlotPage(self.parent, self.figure, LoadFilesPage, self.sub_plots)
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
    
