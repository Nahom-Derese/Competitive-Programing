import sys
import threading
import sys
from collections import *
from itertools import *
from math import *

def suffix_sum(arr):
    n = len(arr)
    suffix = [0] * n
    suffix[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] + arr[i]
    return suffix


def main():
    n, k = [int(i) for i in sys.stdin.readline().split()]
    nums = [int(i) for i in sys.stdin.readline().split()]
    
    suffix = suffix_sum(nums)
    ans = suffix[0]
    suffix = suffix[1:]
    suffix.sort(reverse=True)
    ans += sum(suffix[:k-1])
    print(ans)

if __name__ == '__main__':
    main()
