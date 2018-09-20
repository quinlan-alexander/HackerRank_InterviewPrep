#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    count = 0
    level = 0
    s = list(s)
    for i in range(n):
        if s[i] == 'D':
            level = level - 1
        else:
            level = level + 1
        if level == 0 and s[i] == 'U':
            count = count + 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
