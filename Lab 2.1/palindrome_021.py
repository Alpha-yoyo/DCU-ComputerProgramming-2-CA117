#!/usr/bin/env python3


import sys

def reverse(s):
   return(s[::-1])


def main():
   for line in sys.stdin:
      line = line.lower().strip().strip(".").split()
      line = "".join(line)
      canonical = line.replace(".", "").replace(":", "").replace(",", "").replace("!", "").replace("%", "").replace("#", "").replace("?", "").replace("&", "")

      rev = reverse(canonical)
      if canonical == rev:
         print(True)
      else:
         print(False)


if __name__ == "__main__":
   main()
