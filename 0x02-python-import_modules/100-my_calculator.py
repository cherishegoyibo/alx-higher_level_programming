#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.agrv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] in ops:
        a = int(sys.argv[1])
        op = ops[sys.argv[2]]
        b = int(sys.argv[3])
        res = op(a, b)
        print("{} {} {} = {}".format(a, sys.argv[2], b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
