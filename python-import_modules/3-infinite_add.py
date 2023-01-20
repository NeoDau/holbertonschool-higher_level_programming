#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def arguments(argv):
        x = len(argv)
        sum = 0
        if x == 1:
            print("0")
        else:
            for a in range(1, len(argv)):
                sum += int(argv[a])
            print(sum)
    arguments(sys.argv)
