#!/usr/bin/env python3

import sys
import math

def roots(a, b, c):
    try:
        square = math.sqrt(b * b - (4 * a * c))
        r1 = (-b + square) / (2 * a)
        r2 = (-b - square) / (2 * a)
        return "r1 = {}, r2 = {}".format(r1, r2)
    except:
        return "None"
def main():
    for line in sys.stdin:
        line = line.strip().split()
        a, b, c = int(line[0]), int(line[1]), int(line[2])
        print(roots(a, b, c))

if __name__ == "__main__":
    main()
