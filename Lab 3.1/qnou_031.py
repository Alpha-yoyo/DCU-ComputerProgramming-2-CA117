#!/usr/bin/env python3

import sys

def check_for_qu(word):
   i = 0
   while i < len(word):
      if word[i - 1] == "q":
         if word[i] != "u":
            return(True)
      i += 1

def main():
   qnou = [word.strip() for word in sys.stdin if check_for_qu(word.strip().lower())]
   print("Words with q but no u:", qnou)

if __name__ == "__main__":
   main()
