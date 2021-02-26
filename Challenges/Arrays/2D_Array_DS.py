# Return the sum of maximum hourglass
import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    hg = []
    k = len(arr)
    for i in range(k-2):
        for j in range(k-2):
            hg.append(sum(arr[i][j:j+3]) + sum(arr[i+2][j:j+3]) + arr[i+1][j+1])
    return max(hg)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()