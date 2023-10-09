#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] in ops.items():
        a = int(argv[1])
        ops_ = ops[argv[2]]
        b = int(argv[3])
        result = ops_(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, ops_, b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
