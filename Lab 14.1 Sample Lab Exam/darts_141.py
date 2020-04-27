#!/usr/bin/env python3

import sys

score = []
for line in sys.stdin:
    x, y = line.strip().split()

    r_squrt = int(x) ** 2 + int(y) ** 2
    r = r_squrt ** 0.5
    point = 11 - (r / 20)

    if point > 10:
        score.append(10)
    else:
        score.append(int(point))
print(sum(score))
