#!/usr/bin/env python3

import sys

def main():
   with open(sys.argv[1]) as file:
      file = file.read().split()
      name = file[::3]
      number = file[1::3]
      email = file[2::3]
      info = tuple(zip(number, email))
      contact = dict(zip(name, info))

   for line in sys.stdin:
      line = line.strip()

      if line in contact:
         print("Name:", line)
         print("Phone:", contact[line][0])
         print("Email:", contact[line][1])
      else:
         print("Name:", line)
         print("No such contact")

if __name__ == "__main__":
   main()
