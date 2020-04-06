#!/bin/python3

import math
import os
import random
import re
import sys
import string
# Complete the pangrams function below.


def pangrams(s):
    r = string.ascii_lowercase
    pangram = True
    for letter in r:
        if letter not in s.lower().strip():
            pangram = False
    if pangram == True:
        return 'pangram'
    else:
        return 'not pangram'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
