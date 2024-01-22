#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuple = ()
    length = len(sentence)
    first = sentence[0]
    my_tuple = length, first
    if len(sentence) == 0:
        my_tuple = 0, "None"
        return my_tuple
    else:
        return my_tuple
