#!/usr/bin/env python3

import sys


def main():
   list_strings = []

   line = sys.stdin.readlines()
   for string in line:
      string = string.strip().split()
      club = (" ").join(string[1:-8])
      list_strings.append(club)

   list_club = list_strings
   max_length = len(max(list_club, key=len))

   print ("{:<3s} {:<{}s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}".format("POS", "CLUB", max_length, "P", "W", "D", "L", "GF", "GA", "GD", "PTS"))

   for info in line:
      info = info.strip().split()
      club = (" ").join(info[1:-8])
      print("{:>3s} {:<{}s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}".format(info[0], club, max_length, info[-8], info[-7], info[-6], info[-5], info[-4], info[-3], info[-2], info[-1]))


if __name__ == "__main__":
   main()
