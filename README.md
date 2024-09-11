# Problem Solving Algoritms

This repository is a collection of solutions to various problems in Python.

# Languages Used

Python

# Description

# json_dumps

A custom implementation of the json.dumps() function. This function recursively traverses the structure of the input data to serialize the object into a JSON-formatted string, handling all the different data types; 

Dictionaries - interate through key-value pairs and recursively call json_dumps on the value; <br />
Lists and Tuples -  iterate through elements and recursively call json_dumps on each element; and <br />
Strings, Integers, Floats, Booleans, and None - convert these directly into their JSON string representations.

The "seperators" functionality has also been implemented into json_dumps i.e. json_dumps({"one": 1, "two": 2, "three": 3}, separators=('+','-')) == '{"one"-1+"two"-2+"three"-3}'

# boggle

 <div align="justify">
A function designed to test whether a string is a valid solution in the Boggle word game (the objective of Boggle is to find valid words on a board of lettered dice by connecting adjacent letters without repeating positions, but in our case any valid string will satisfy). 

When given a list of lists and a string, this function will check that this list forms a valid board (i.e. only contains alphabetic characters) and that every character in the string can be found on the board list. The function then converts the board to a series of tuple index positions [[(0,0), (0,1)], [(1,0),(1,1)]] which is assigned to each character in a dictionary. 

Using the string, the function then uses a recursive cartesian product operation to discover all possible paths through the board to get the string, each path represented by a list of tuples. Finally, each path is looped over to check that duplicate index positions are not used and that each movement is between +1 to -1 in both the x and y direction. Once a valid path is found, True is returned as the string is a valid solution to the board, else False for invalid. 
</div>
