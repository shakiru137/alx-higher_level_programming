#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    temp = [0] * len(my_list)
    for i in range(len(my_list)):
        temp[i] = my_list[len(my_list) - i - 1]
    for i in range(len(temp)):
        print("{:d}".format(temp[i]))
