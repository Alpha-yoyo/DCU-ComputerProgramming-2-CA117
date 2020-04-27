#!/usr/bin/env python3

import sys

def main():
   with open(sys.argv[1]) as file:
      file = file.read().split()
      name = file[::2]
      number = file[1::2]
      contact = dict(zip(name, number))

   for line in sys.stdin:
      line = line.strip()
      if line in contact:
         print("Name:", line)
         print("Phone:", contact[line])
      else:
         print("Name:", line)
         print("No such contact")

if __name__ == "__main__":
   main()
