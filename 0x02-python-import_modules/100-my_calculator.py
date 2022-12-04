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
    
    op = av[2]
    for i in range(4):
        if op == op_list[i]:
            func = func_list[i]
            ans = func(int(av[1]), int(av[3]))
            print("{:d}".format(ans))
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
