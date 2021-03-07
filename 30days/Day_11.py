
import math
import os
import random
import re
import sys

def hourglass(arr):
    hg = []
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            hg.append(sum(arr[i][j:j+3]) + sum(arr[i+2][j:j+3]) + arr[i+1][j+1])
    print(max(hg))

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    hourglass(arr)