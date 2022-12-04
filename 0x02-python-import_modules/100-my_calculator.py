#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    ac = len(sys.argv) - 1
    av = sys.argv
    op_list = ["+", "-", "*", "/"]
    func_list = [add, sub, mul, div]
    if ac != 3:
        print("Usage: {:s} <a> <operator> <b>".format(av[0]))
        exit(1)

    for i in range(len(op_list)):
        if av[2] == op_list[i]:
            ans = func_list[i](int(av[1]), int(av[3]))
            print("{:s} {:s} {:s} = {:d}".format(av[1], av[2], av[3], ans))
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
