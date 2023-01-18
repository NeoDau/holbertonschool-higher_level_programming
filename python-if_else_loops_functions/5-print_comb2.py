#!/usr/bin/python3
def add(num):
    return f"{num:02d}"
for num in range(0, 100):
    if num > 0:
        print(", ", end="")
#    print(add(num), end="")
    print("{}".format(add(num)), end="")

