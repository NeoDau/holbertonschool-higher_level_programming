#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    for a in range(x):
        try:
            print(my_list[a], end="")
        except IndexError:
            print()
            return a
        else:
            a += 1
    print()
    return a
