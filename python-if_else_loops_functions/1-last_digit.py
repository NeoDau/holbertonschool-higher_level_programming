#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = number
if x % 10 > 5:
    print(f"Last digit of {x} is {x % 10} and is greater than 5")
if x % 10 == 0:
    print(f"Last digit of {x} is {x % 10} and is 0")
if x % 10 < 6 and number % 10 != 0 and number > 0:
    print(f"Last digit of {x} is {x % 10} and is less than 6 and not 0")
if x < 0:
    i = number * -1
    print(f"Last digit of {x} is {i % 10 * -1} and is less than 6 and not 0")
