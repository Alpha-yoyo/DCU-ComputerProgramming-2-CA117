#!/usr/bin/env python3

import sys

def main():
    list1 = sys.stdin.readline().split()
    list2 = sys.stdin.readline().split()

    position = []
    count = 0
    for i, j in zip(list1, list2):
        if i == j:
            position.append(count)
        count += 1
    print(position)

if __name__ == "__main__":
    main()
