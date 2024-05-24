#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is {number % 10}",
        f"and is greater than 5" if number % 10 > 5 else
        f"and is 0" if number % 10 == 0 else
        f"and is less than 6 and not 0")
