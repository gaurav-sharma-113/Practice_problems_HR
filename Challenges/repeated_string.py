# Repeated String
# There is a string, s, of lowercase English letters that is repeated 
# infinitely many times. Given an integer, n, find and print the number 
# of letter a's in the first  letters of the infinite string.
#
# Example
# s = 'abcac'
# n = 10
#
# The substring we consider is 'abcacabcac', the first 10 characters 
# of the infinite string. There are  occurrences of a in the substring.
#
# Function Description
# repeatedString has the following parameter(s):
# s: a string to repeat
# n: the number of characters to consider
#
#Returns
# int: the frequency of a in the substring

# Input Format
# The first line contains a single string, s.
# The second line contains an integer, n.

#!/bin/python3

import math
import os
import random
import re
import sys
import pdb

# Complete the repeatedString function below.
def repeatedString(s, n):
    if n%len(s)==0:
        return s.count('a')*(n//len(s))
    else:
        return (s.count('a')*(n//len(s)) + s[:(n%len(s))].count('a'))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #s = 'aba'
    #n = 10
    s = input()

    n = int(input())

    result = repeatedString(s, n)

    #fptr.write(str(result) + '\n')

    #fptr.close()