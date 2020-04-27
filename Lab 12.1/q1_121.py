#!/usr/bin/env python

import sys

def main():
    word = sys.argv[1]
    num = int(sys.argv[2])
    num = num % len(word)
    print(word[num:] + word[:num])

if __name__ == "__main__":
    main()
