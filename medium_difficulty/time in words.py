#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
time = {'1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight',
        '9': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve',
        '13': 'thirteen', '14': 'fourteen', '16': 'sixteen',
        '17': 'seventeen', '18': 'eighteen', '19': 'nineteen', '20': 'twenty',
        '21': 'twenty one', '22': 'twenty two', '23': 'twenty three', '24': 'twenty four',
        '25': 'twenty five', '26': 'twenty six', '27': 'twenty seven', '28': 'twenty eight',
        '29': 'twenty nine',
        }


def timeInWords(h, m):
    if m == 0:
        return (str(time[str(h)]) + " o' clock")
    if m < 30:
        if m == 1:
            return (str(time[str(m)]) + " minute past " + str(time[str(h)]))
        elif m == 15:
            return ('quarter past ' + str(time[str(h)]))
        else:
            return (str(time[str(m)]) + " minutes past " + str(time[str(h)]))
    if m == 30:
        return ('half past ' + str(time[str(h)]))
    if m > 30:
        mm = 60 - m
        if h == 12:
            hh = 1
        else:
            hh = h+1
        if mm == 1:
            return (str(time[str(m)]) + " minute to " + str(time[str(hh)]))
        elif mm == 15:
            return ('quarter to ' + str(time[str(hh)]))
        else:
            return (str(time[str(mm)]) + " minutes to " + str(time[str(hh)]))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
