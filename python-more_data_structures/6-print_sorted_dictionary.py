#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for x, a in sorted(a_dictionary.items()):
        print("{}: {}".format(x, a))
