#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    av = len(sys.argv) - 1
    if av == 0:
        print("{:d} arguments.".format(av))
    else:
        if av == 1:
            print(f"{av} argument:")
        else:
            print("{:d} arguments:".format(av))
        for i in range(av):
            print("{:d}: {:s}".format(i + 1, sys.argv[i + 1]))
