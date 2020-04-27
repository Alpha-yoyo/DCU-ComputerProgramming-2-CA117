#!/usr/bin/env python3

import sys
import re

def main():
    for line in sys.stdin:
        line = line.strip()
        words = " ".join(re.findall('[A-Z][^A-Z]*', line))
        print(words.lower().capitalize())

if __name__ == "__main__":
    main()
