#!/usr/bin/env python3

import sys


def main():
   for line in sys.stdin:
      line = line.strip()
      consonants = ["by", "cy", "dy", "fy", "gy", "hy", "jy", "ky", "ly", "my", "ny", "py", "qy", "ry", "sy", "ty", "vy", "wy", "xy", "zy"]

      if line[-2:] in ["ch", "sh"]:
         print(line + "es")

      elif line[-1:] in ["x", "s", "z"]:
         print(line + "es")

      elif line[-2:] in consonants:
         print(line[0:-1] + "ies")

      elif line[-2:] in ["fe"]:
         print(line[0:-2] + "ves")

      elif line[-1:] in ["f"]:
         print(line[0:-1] + "ves")

      elif line[-1:] in ["o"]:
         print(line + "es")
      else:
         print(line + "s")


if __name__ == "__main__":
   main()
