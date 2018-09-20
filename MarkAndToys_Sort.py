#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maximumToys function below.
def maximumToys(prices, k):
    sortedPrices = sorted(i for i in prices if i <= k)
    moneySpent = 0
    countToys = 0
    index = 0
    for i in range(len(sortedPrices)):
        if (moneySpent + sortedPrices[index]) <= k:
            moneySpent += sortedPrices[index]
            countToys += 1
            index += 1
        else:
            break
    return countToys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
