#!/usr/bin/python3

# Imports
import xml.etree.ElementTree as ET

# Variable declarations

# Classes

# Functions
def file_to_tree(filename):
    return ET.parse(filename)

def root_from_tree(tree):
    return tree.getroot()


def parse_file(filename):
    root = root_from_tree(file_to_tree(filename))

# Main

if __name__ == "__main__":
    parse_file("activity.xml")
