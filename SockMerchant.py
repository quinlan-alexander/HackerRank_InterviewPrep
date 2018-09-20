#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    socks = {}
    for i in range(n):
        if ar[i] in socks:
            socks[ar[i]] = socks[ar[i]] + 1
            continue
        socks.update({ar[i]: 1})

    pairCount = 0
    for value in socks.values():
        pairCount = pairCount + value // 2

    return pairCount


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
