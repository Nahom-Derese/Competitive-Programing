import sys
from collections import *
from itertools import *
from math import *


def solve_problem(nums, n, l, k):
    pass


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(sys.stdin.readline().strip())
        nums = [int(i) for i in sys.stdin.readline().split()]

        for _ in range(int(input())):
            l, k = [int(i) for i in sys.stdin.readline().split()]
            print(solve_problem(nums, n, l, k), end=" ")
        print()
