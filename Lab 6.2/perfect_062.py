#!/usr/bin/env python 3

import sys
import math
def sumFac(n):
    results = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            results.add(i)
            results.add(int(n / i))
    return sum(sorted(results)[0:-1])

def isperfect(n1):
   return n1 == sumFac(n1)
def main():
    for line in sys.stdin:
        line = int(line.strip())
        print(isperfect(line))

if __name__ == "__main__":
    main()
