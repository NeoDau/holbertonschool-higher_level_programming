#!/usr/bin/python3
if __name__ == "__main__":
    import sys
def argPrint(argv):
    x = len(argv) - 1
    if x == 0:
        print(x, "arguments.")
    elif x == 1:
        print(x, "argument:")
    else:
        print(x, "arguments")
    for a in range(1, x + 1):
        print("{}: {}".format(a, argv[a]))
argPrint(sys.argv)
