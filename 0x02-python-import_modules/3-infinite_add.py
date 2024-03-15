#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    inf_add = 0
    for i in range argv[1:]:
        inf_add += int(i)
        print("{}".format(inf_add))
