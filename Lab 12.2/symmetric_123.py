#!/usr/bin/env python3

import sys

def main():
    lis = sys.stdin.readlines()
    tmp = []
    for x in range(1, (len(lis) + 1) // 2):
        tmp.append(lis.pop(x))

    for x in range(len(tmp)):
        lis.append(tmp.pop())

    for name in lis:
        print(name.strip())

if __name__ == "__main__":
    main()
