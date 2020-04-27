#!/usr/bin/env python3

import sys

def main():
    dart = {}
    for line in sys.stdin:
        line = line.strip().split()
        name, score = " ".join(line[0:-1]), line[-1].split(",")
        total = 0

        for point in score:
            if point == "X":
                total += 0
            else:
                total += int(point)

        average = total / 6
        dart[name] = average

    for k, v in sorted(dart.items(), key=lambda x: x[1], reverse=True):
        print(("{} {:.1f}").format(k, v))

if __name__ == "__main__":
    main()
