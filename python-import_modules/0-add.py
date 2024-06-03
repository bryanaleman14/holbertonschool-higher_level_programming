#!/usr/bin/python3
from add_0 import add
if __name__ == "__main__":
    if add(1, 2):
        a = 1
        b = 2
        print("{}".format(add(a, b)))
    else:
        print("{}".format(add(a, b)))
