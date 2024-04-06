import sys
from collections import *
from itertools import *
from math import *
from bisect import bisect_left, bisect_right

def binary_search(arr, target):
    left, right = [1, 10**9]
    while left <= right:
        mid = left + (right - left) // 2
        less = bisect_right(arr, mid)
        if less == target:
            return mid
        elif less < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

n, k = [int(i) for i in sys.stdin.readline().split()]

nums = sorted([int(i) for i in sys.stdin.readline().split()])

print(binary_search(nums, k))
