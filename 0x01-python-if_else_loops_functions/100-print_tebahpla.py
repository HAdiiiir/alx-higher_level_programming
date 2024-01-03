#!/usr/bin/python3

for char in range(ord('Z'), ord('A') - 1, -1):
    print("{}{}".format(chr(char).lower(), chr(char)), end="")
