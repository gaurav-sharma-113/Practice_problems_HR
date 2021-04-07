#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

def bubble_sort(arr):
    swap_counter = 0
    for num in range(len(arr)-1, 0, -1):
        for i in range(num):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap_counter +=1
    return swap_counter

print ("Array is sorted in {} swaps.".format(bubble_sort(a)))
print ("First Element: {}".format(a[0]))
print ("Last Element: {}".format(a[-1]))