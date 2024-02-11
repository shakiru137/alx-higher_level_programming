#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        numOfEl = 0
        for i in range(x):
            print(my_list[i], end="")
            numOfEl += 1
        print()
        return numOfEl
    except IndexError:
        print()
        return numOfEl
