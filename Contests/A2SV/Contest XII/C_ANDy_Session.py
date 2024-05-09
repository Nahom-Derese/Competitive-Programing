import sys
from collections import *
from itertools import *
from math import *


def solve_problem(n, k, nums):
    numsAND = nums[0]
    for i in range(1, n):
        numsAND &= nums[i]

    possible = []
    for i in range(31):
        toggles_needed = 0
        for num in nums:
            toggles_needed += (not bool(num & (1 << i)))
        if toggles_needed and toggles_needed <= k:
            possible.append((i, toggles_needed))

    possible.sort(reverse=True)

    # print(possible)
    for i, toggles in possible:
        if k - toggles >= 0:
            numsAND += (1 << i)
            k -= toggles
        if not k:
            break
    return numsAND


if __name__ == '__main__':
    for i in range(int(input())):
        n, k = [int(i) for i in sys.stdin.readline().split()]
        nums = [int(i) for i in sys.stdin.readline().split()]

        print(solve_problem(n, k, nums))
