#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        position = -1
        line = list(line.strip())

        for char in line:
            position += 1
            if char in "aeiou":
                if line[position + 1] == "p":
                    del line[position + 1:position + 3]

        print("".join(line))

if __name__ == "__main__":
    main()
