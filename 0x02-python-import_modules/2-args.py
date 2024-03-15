#!/usr/bin/python3
import sys
if __name__ == "__main__":
    numb_arg = len(sys.argv) - 1
    if numb_arg == 0:
        print("0 arguments.")
    elif numb_arg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(numb_arg))
    for i in range(numb_arg):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
