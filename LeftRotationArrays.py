#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def array_left_rotation(a, n, k):
    return a[k:]+a[:k]

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')