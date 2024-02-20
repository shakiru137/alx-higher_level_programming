#!/usr/bin/python3
"""
Function to read the contents of a text file and print it to stdout.

Args:
    filename (str, optional): The name of the file to read. Defaults to 'my_file_0.txt'.
"""

def read_file(filename="my_file_0.txt"):
    """
    Read the contents of a text file and print it to stdout.

    Args:
        filename (str, optional): The name of the file to read. Defaults to 'my_file_0.txt'.
    """
    with open(filename, 'r', encoding="UTF8") as f:
        read_data = f.read().strip()
        print(read_data)

read_file()

