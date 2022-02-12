#!/usr/bin/python3
"""
Author: Javier Millan
This script takes in the contents of a text box ipywidget as input, and uses it as a regular expression 
to find all matches of that string in  the P3_argonaut.gb file.

"""
from __future__ import print_function
import ipywidgets as widgets
from IPython.display import display
from ipywidgets import interact, interactive, fixed, interact_manual

import re


def parse_regex(path, pattern):
    """Return a list of matches in each line of the path file to the pattern, using regular expressions.
    path: relative path of the text file
    pattern: string with the regex pattern to match
    """
    with open(path, 'r') as f:
        lines = f.readlines() # Creates a list of lines
        matches = [] # Empty list to store all accession numbers
        for line in lines:
            match = re.findall(pattern, line) # Attempts to match pattern. 
            if match:
                matches.append(match) # Appends to the list the found matches in each line as a list
    return matches


def regex_widget(precedes, match, follows):
    """Checks if the regular expression product of combining the three inputs is valid, then 
    tries to pass it as an argument for parse_regex().
    precedes: pattern preceding the match
    match: pattern to match
    follows: pattern succeeding the match
    """
    path = "files/P3_argonaut.gb"
    precedes = "(?<=" + precedes + ")"
    follows = "(?=" + follows + ")"
    pattern = precedes + match + follows
    valid = False
    if pattern != "":
        try:
            re.compile(pattern)
            result = parse_regex(path, pattern)
            valid = True
        except re.error:
            pass
        if valid == True:
            print("Your pattern is: ", pattern, "\n", "matches:", result)
        if valid == False:
            print("Your pattern: ", pattern, "is invalid")
    