#!/usr/bin/python3
import dis
import sys
import types

def print_hidden_names(file_path):
    with open(file_path, 'rb') as file:
        code = compile(file.read(), file_path, 'exec')

    for item in code.co_names:
        if not item.startswith('__'):
            print(item)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./4-hidden_discovery.py <path_to_hidden_4.pyc>")
    else:
        print_hidden_names(sys.argv[1])
