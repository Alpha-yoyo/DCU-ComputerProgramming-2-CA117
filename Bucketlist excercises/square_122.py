#!/usr/bin/env python3

import math
import sys

def distance(point1, point2):
   return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def main():
   x = []
   y = []
   for line in sys.stdin:
      line = line.strip().split()
      x.append(int(line[0]))
      y.append(int(line[1]))

   point1 = x[0], y[0]
   point2 = x[1], y[1]
   point3 = x[2], y[2]
   combo_points = ((point1, point2), (point2, point3), (point1, point3))
   dict_dist = {
      combo_points[0]: distance(point1, point2),
      combo_points[1]: distance(point2, point3),
      combo_points[2]: distance(point1, point3),
   }

   list_dist = [distance(point1, point2), distance(point2, point3), distance(point1, point3)]
   longest_dist = max(list_dist)
   seen = []
   for keys in dict_dist:
      if dict_dist[keys] == longest_dist:
         value1 = keys[0][0] + keys[1][0], keys[0][1] + keys[1][1]
      else:
         for points in keys:
            if points not in seen:
               seen.append(points)
            elif points in seen:
               value2 = points

   point4 = value1[0] - value2[0], value1[1] - value2[1]
   print(point4[0], point4[1])

if __name__ == "__main__":
   main()
