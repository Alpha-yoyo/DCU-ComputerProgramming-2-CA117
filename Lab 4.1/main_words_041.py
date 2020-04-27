#!/usr/bin/env python3

import sys
from string import punctuation

def main():
   line = sys.stdin.read().lower().split()
   line = [word.lower().strip(punctuation) for word in line]
   words = [word.lower().strip(punctuation) for word in line if len(word) > 3]
   set_words = sorted(set(words))

   for word in set_words:
      if line.count(word) > 2:
         print("{:>9s} : {:2d}".format(word, line.count(word)))

if __name__ == "__main__":
   main()
