#!/usr/bin/env python3

import sys

def main():
    vowel_count = {}
    for line in sys.stdin:
        line = line.strip()
        double_vowel = ["aa", "ee", "ii", "oo", "uu"]

        total = 0
        for vowel in double_vowel:
            total += line.count(vowel)
        vowel_count[line] = total

    sort = sorted(vowel_count.items(), key=lambda x: x[1])

    print(sort[-1][0])

if __name__ == "__main__":
    main()
