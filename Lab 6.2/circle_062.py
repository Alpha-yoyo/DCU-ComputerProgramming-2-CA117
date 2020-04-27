#1/usr/bin/env python3

import math

def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
    distsqr = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    sumrad = r1 + r2

    return distsqr < sumrad
