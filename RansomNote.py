#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazineWords = {}
    for i in range(len(magazine)):
        if magazine[i] in magazineWords:
            magazineWords[magazine[i]] += 1
        else:
            magazineWords[magazine[i]] = 1

    for i in range(len(note)):
        if note[i] in magazineWords:
            if magazineWords[note[i]] == 0:
                return "No"
            else:
                magazineWords[note[i]] -= 1
        else:
            return "No"
    return "Yes"


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
