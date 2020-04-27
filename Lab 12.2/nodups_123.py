#!/usr/bin/env python3

import sys
from string import punctuation

def main():
    seen = []

    for line in sys.stdin:
        line = line.strip().split()
        pos = -1

        for word in line:
            word = word.strip(punctuation).lower()
            pos += 1
            if word not in seen:
                seen.append(word)
            else:
                line[pos] = "."

        print(" ".join(line))

if __name__ == "__main__":
    main()
