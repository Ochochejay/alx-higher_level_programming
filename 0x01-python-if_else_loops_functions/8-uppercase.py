#!/usr/bin/python3
def uppercase(str):
    for s in str:
        c = ord(s)
        if c >= 97 and c <= 122:
            c = ord(s) - 32
        print("{:s}".format(chr(c)), end="")
    print(end="\n")
