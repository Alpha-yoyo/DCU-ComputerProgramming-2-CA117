#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        time, num = line.strip().split()
        hrs, mins = time.split(":")

        total_min = (int(hrs) * 60 + int(mins)) - int(num)

        if total_min > 60:
            hrs = total_min // 60
            if hrs == 24:
                hrs = 0
            mins = total_min % 60
            print("{:02d}:{:02d}".format(hrs, mins))

        elif total_min < 0:
            change = 1440 + total_min
            hrs = change // 60
            mins = change % 60
            print("{:02d}:{:02d}".format(hrs, mins))

        else:
            hrs = 0
            print("{:02d}:{:02d}".format(hrs, total_min))

if __name__ == "__main__":
    main()
