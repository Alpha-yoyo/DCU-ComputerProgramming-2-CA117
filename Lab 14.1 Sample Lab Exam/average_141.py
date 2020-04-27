#!/usr/bin/env python3

import sys

line = sys.stdin.read().split()
leng = []
for word in line:
    leng.append(len(word))

average = sum(leng) / len(leng)

print("Average: {:.2f}".format(average))

for word2 in line:
    if len(word2) > average:
        print(word2)
