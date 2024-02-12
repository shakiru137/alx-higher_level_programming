#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Function that prints My name is <first name> <last name>

    Parameters:
    first_name: the first name
    last_name=None: the second name

    Returns:
    nothing

    Exception:
    first_name and last_name must be strings otherwise, raise a
    TypeError exception with the message first_name must be a
    string or last_name must be a string
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print("My name is {:s} {:s}".format(first_name, last_name or ""))
