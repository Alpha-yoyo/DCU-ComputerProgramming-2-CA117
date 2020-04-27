#!/usr/bin/env python3

import sys
sys.setrecursionlimit(100000)

def floodfill(image, x, y):
    row = len(image)
    col = len(image[0])

    if image[x][y] != "-":
        return
    image[x][y] = ""

    if x > 0:
        floodfill(image, x - 1, y)

    if x < row - 1:
        floodfill(image, x + 1, y)

    if y > 0:
        floodfill(image, x, y - 1)

    if y < col - 1:
        floodfill(image, x, y + 1)

def main():
    row, col = sys.stdin.readline().split()
    row, col = int(row), int(col)
    list_lines = sys.stdin.read().split()

    total = 0
    image = [list(row) for row in list_lines]
    for r in range(row):
        for c in range(col):
            if image[r][c] == "-":
                floodfill(image, r, c)
                total += 1
    print(total)

if __name__ == '__main__':
    main()
