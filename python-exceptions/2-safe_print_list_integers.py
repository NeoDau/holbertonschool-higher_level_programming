#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    pi = 0
    try:
        for n in range(x):
            print("{:d}".format(my_list[n]), end="")
            pi += 1
    except (ValueError, TypeError):
        pass
    print()
    return pi

            
