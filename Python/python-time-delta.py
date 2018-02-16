#!/bin/python3

import sys
import datetime.datetime as dt

def time_delta(t1, t2):
    format = '%a %d %b %Y %H:%M:%S %z'
    diff = abs((dt.strptime(t1, format) - dt.strptime(t2, format)))
    return int(diff.total_seconds())

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        t1 = input().strip()
        t2 = input().strip()
        delta = time_delta(t1, t2)
        print(delta)
