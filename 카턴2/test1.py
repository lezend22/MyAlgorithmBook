#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solution' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER x
#  2. INTEGER y
#  3. INTEGER z
#

def solution(x, y, z):
    # Write your code here
    if y > x:
        x, y = y, x

    max_ = x

    rem = z
    rem = rem - (x - y)

    if rem >= 0:
        if rem % 2:
            rem -= 1
            max_ += rem // 2
        else:
            max_ += rem // 2
    else:
        return -1

    return max_


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x = int(input().strip())

    y = int(input().strip())

    z = int(input().strip())

    result = solution(x, y, z)

    fptr.write(str(result) + '\n')

    fptr.close()
