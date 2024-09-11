# Problem Solving Algoritms

This repository is a collection of solutions to various problems in Python.

# Languages Used

Python

# Description

# json_dumps

A custom implementation of the json.dumps() function. This function recursively traverses the structure of the input data to serialize the object into a JSON-formatted string, handling all the different data types; 

Dictionaries - interate through key-value pairs and recursively call json_dumps on the value;
Lists and Tuples -  iterate through elements and recursively call json_dumps on each element; and
Strings, Integers, Floats, Booleans, and None - convert these directly into their JSON string representations.

The "seperators" functionality has also been implemented into json_dumps i.e. json_dumps({"one": 1, "two": 2, "three": 3}, separators=('+','-')) == '{"one"-1+"two"-2+"three"-3}'
