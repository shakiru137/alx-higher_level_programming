#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Function to add two integers

    Parameters:
    a (int or float): first number
    b (int or float: second number (initialized to 98 if not provided)

    Returns:
    The sum of a and b in (int)

    Raises:
    TypeError: If a or b are not ints or floats
    """
    if not isinstance(a, (int, float)):
            raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
