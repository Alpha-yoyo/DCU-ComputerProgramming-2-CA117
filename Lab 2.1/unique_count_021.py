#!/usr/bin/env python3

import sys

def main():
   seen = []
   line = sys.stdin.read().split()
   for words in line:
      words = words.lower()
      words = words.strip(",")
      words = words.strip(".")
      if words != "--":
         if words not in seen:
            seen.append(words)
   print(len(seen))


if __name__ == "__main__":
   main()
