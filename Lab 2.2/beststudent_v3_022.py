#!/usr/bin/env python3

import sys

def main():
   with open(sys.argv[1]) as file:
      line = file.readlines()

   list_scores = []
   for students in line:
      students = students.strip().split()
      try:
         list_scores.append(int(students[0]))
      except:
         print("Invalid mark {:s} encountered. Skipping.".format(students[0]))

   best_score = max(list_scores)

   list_names = []
   for name in line:
      name = name.strip()
      if str(best_score) in name:
         list_names.append(name[3:])

   print("Best student:", list_names[0])
   print("Best mark:", best_score)

if __name__ == "__main__":
   main()
