#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s1Letters = {}
    s1List = list(s1)
    s2List = list(s2)

    for i in range(len(s1List)):
        if s1List[i] in s1Letters:
            s1Letters[s1List[i]] += 1
        else:
            s1Letters[s1List[i]] = 1

    for i in range(len(s2List)):
        if s2List[i] in s1Letters:
            return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
