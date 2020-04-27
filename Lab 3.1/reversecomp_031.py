#!/sur/bin/env python3

import sys

def reverse(s):
   return(s[::-1])

def main():
   list_lines = sys.stdin.read().split()
   words_length = {word.lower(): word for word in list_lines if len(word) > 4}
   palindrome = [words_length[word1] for word1 in sorted(words_length) if reverse(word1) in words_length]

   print(palindrome)

if __name__ == "__main__":
   main()
