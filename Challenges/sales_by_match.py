# Sales by Match
#
# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
#
# Example
# There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .
#
# Function Description
#
# Complete the sockMerchant function in the editor below.
#
# sockMerchant has the following parameter(s):
# int n: the number of socks in the pile
# int ar[n]: the colors of each sock
# 
# Returns
# int: the number of pairs
#
# Input Format
# The first line contains an integer , the number of socks represented in .
# The second line contains  space-separated integers, , the colors of the socks in the pile.


#!/bin/python3

import math
import os
import random
import re
import sys
import pdb

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    dict_count = {}
    for i in ar:
        if i in dict_count:
            dict_count[i] += 1
        else:
            dict_count[i] = 1
    return sum([int(i/2) for i in dict_count.values()])
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    #fptr.write(str(result) + '\n')

    #fptr.close()