#!/usr/bin/python3
for x in reversed(range(97, 123)):
    if x % 2:
        x -= 32
    print("{:c}".format(x), end="")
