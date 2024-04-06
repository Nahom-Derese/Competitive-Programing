import sys
from collections import *
from itertools import *
from math import *


res = []



n = int(sys.stdin.readline().strip())

nums = [int(i) for i in sys.stdin.readline().split()]

def backtrack(path, candidate):
    global res
    global nums
    global ans

    if len(path) == len(nums):
        print(*path)
        exit()
    
    for i in range(len(candidate)):
        if (not path) or ((path[-1] % 3 == 0 )and candidate[i] == path[-1] // 3) or (candidate[i] == path[-1] * 2):
            backtrack(path + [candidate[i]], candidate[:i] + candidate[i+1:])


backtrack([], nums)
