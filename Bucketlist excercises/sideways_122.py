#!/usr/bin/env python3

import sys

line = sys.stdin.read().split()
vir_line = ["".join(row) for row in zip(*line)]
sorted_list = sorted(vir_line, key=lambda x: x.lower())

for i in range(len(line)):
   for j in range(len(vir_line)):
      print(sorted_list[j][i], end='')
   print()
