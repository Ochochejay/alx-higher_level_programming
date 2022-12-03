#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    av = len(sys.argv) - 1
    add = 0
    if av != 0:
        i = 1
        while i <= av:
            add += int(sys.argv[i])
            i += 1
    print("{:d}".format(add))
