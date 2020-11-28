#!/usr/bin/python3

# Imports
import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import ttk
import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk
# Variable declarations

# Classes
class PlotPage(Frame):
    def __init__(self, parent, figure, main_menu_class, sub_plots):
        Frame.__init__(self, parent)
    
        self.figure = figure
        self.main_menu_class = main_menu_class
        self.sub_plots = sub_plots
    
        button = ttk.Button(self, text="Back", command=self.back)
        button.pack()

        parent.geometry("700x550")
        canvas = FigureCanvasTkAgg(figure, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    def back(self):
        main_menu = main_menu_class(self.parent, self.figure, self.sub_plots) 
        self.pack_forget()
        main_menu.pack()

# Functions
def file_to_tree(filename):
    return ET.parse(filename)

def root_from_tree(tree):
    return tree.getroot()

def handle_laps(laps):
    tracks = []
    for lap in laps:
        tracks += lap.findall('{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Track')
    return tracks

def handle_tracks(tracks):
    track_points = []
    for track in tracks:
        track_points += track.findall('{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Trackpoint')
    return track_points

def handle_points(points):
    hbs, watts = [], []
    for point in points:
        hb, watt = handle_point(point)
        hbs.append(hb)
        watts.append(watt)

    hbs = np.array(hbs)
    watts = np.array(watts)
    return hbs, watts

def handle_point(point):
    hb = point.find('{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}HeartRateBpm')
    hb = hb.find('{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Value').text
    watt = point.find('{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Extensions')
    watt = watt.find('{http://www.garmin.com/xmlschemas/ActivityExtension/v2}TPX')
    watt = watt.find('{http://www.garmin.com/xmlschemas/ActivityExtension/v2}Watts').text
    watt = float(watt)
    hb = float(hb)
    return hb, watt

def parse_file(filename):
    root = root_from_tree(file_to_tree(filename))
    activity = root[0][0]
    laps = activity.findall("{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Lap")
    training_id = activity.find("{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Id").text
    tracks = handle_laps(laps)
    track_points = handle_tracks(tracks)
    hbs, watts = handle_points(track_points)
    ffit = values_fit(hbs, watts)
    return hbs, watts, ffit, training_id

def values_fit(x, y):
    xn = np.array(x)
    yn = np.array(y)
    coefs = poly.polyfit(x, y, 1)
    ffit = poly.Polynomial(coefs)
    return ffit

def create_plot(x, y, ffit):
    plt.plot(x, y, 'o', x, ffit(x))
    plt.xlabel("Hbs")
    plt.ylabel("Watts")
    plt.show()

# Main

if __name__ == "__main__":
    hbs, watts, ffit = parse_file("activity.xml")
    create_plot(hbs, watts, ffit)


