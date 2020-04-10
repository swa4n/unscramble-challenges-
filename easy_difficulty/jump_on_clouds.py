#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c):
    jumps = 0
    position = 0
    if len(c) == 2:
        return 1
    while position < len(c)-2:
        if c[position+2] == 0:
            position += 2
        else:
            if position == len(c)-2:
                return c[position]
            position += 1
        jumps += 1
    if position == len(c)-1:
        return jumps
    if position == len(c)-2:
        return jumps+1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    fptr.write(str(result) + '\n')
    fptr.close()
