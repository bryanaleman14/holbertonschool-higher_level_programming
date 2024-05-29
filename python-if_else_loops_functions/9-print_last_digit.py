#!/usr/bin/python3
def print_last_digit(number):
    if isinstance(number, str):
        return -1
    else:
        number_str = str(number)
        print("{}".format(number_str[-1:]), end='')
        return number_str[-1:]
