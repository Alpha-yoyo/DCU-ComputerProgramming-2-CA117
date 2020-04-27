#!/usr/bin/env python3

import sys
from string import punctuation

def sorter(t):
   return(t[1])

def main():
   line = sys.stdin.read().lower().split()
   line = [word.strip(punctuation) for word in line]
   string = "".join(line)
   vowels = set("aeiou")
   freq = [string.count(char) for char in vowels]
   vowel_count = dict(zip(vowels, freq))

   max_vowels = len(max(vowel_count.keys(), key=len))
   max_freq = len(str(max(vowel_count.values())))

   for (vowels, freq) in sorted(vowel_count.items(), key=sorter, reverse=True):
      print("{:>{}s} : {:{}d}".format(vowels, max_vowels, freq, max_freq))

if __name__ == "__main__":
   main()
