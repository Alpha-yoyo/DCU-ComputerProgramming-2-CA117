#!/usr/bin/env python3

import sys
from string import punctuation

def main():
   line = sys.stdin.read().split()
   words = [word.lower().strip(punctuation) for word in line]
   set_words = sorted(set(words))

   for char in set_words:
      print(char, ":", words.count(char))

if __name__ == "__main__":
   main()
