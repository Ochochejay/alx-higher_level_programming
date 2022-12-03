#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    av = len(sys.argv)
    if av == 1:
        print("{:d} arguments.".format(0))
    else:
        print("{:d} arguments:".format(av-1))
        for i in range(av-1):
            print("{:d}: {:s}".format(i+1, sys.argv[i+1]))
