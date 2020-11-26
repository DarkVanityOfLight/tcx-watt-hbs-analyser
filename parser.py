#!/usr/bin/python3

# Imports
import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import ttk
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

# Variable declarations

# Classes
class PlotPage(Frame):
    def __init__(self, parent, figure):
        Frame.__init__(self, parent)
    
        canvas = FigureCanvasTkAgg(figure, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


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
    return hbs, watt

def handle_point(point):
    hb = point.find('{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}HeartRateBpm')
    hb = hb.find('{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Value').text
    watt = point.find('{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Extensions')
    watt = watt.find('{http://www.garmin.com/xmlschemas/ActivityExtension/v2}TPX')
    watt = watt.find('{http://www.garmin.com/xmlschemas/ActivityExtension/v2}Watts').text
    return hb, watt

def parse_file(filename):
    root = root_from_tree(file_to_tree(filename))
    activity = root[0][0]
    laps = activity.findall("{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Lap")
    tracks = handle_laps(laps)
    track_points = handle_tracks(tracks)
    hbs, watt = handle_points(track_points)

def create_plot(x, y, name):
    f = Figure(figsize(len(x), len(y)), dpi=100)
    a = f.add_subplot()
    a.plot(x, y)
    return f

# Main

if __name__ == "__main__":
    parse_file("activity.xml")
    root().title("Training Data") # TODO Get the training date


