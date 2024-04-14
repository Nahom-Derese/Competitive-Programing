import sys
from collections import *
from itertools import *
from math import *

n = 0
graph = defaultdict(list)

def inbound(i):
    return 0 <= i < n

def solve_problem():
    global n
    n = int(sys.stdin.readline().strip())
    
    nums = [int(i) for i in sys.stdin.readline().split()]
    ans = [-1] * n
    
    for i in range(n):
        right = i+nums[i]
        left = i-nums[i]

        if inbound(right) and nums[right] % 2 != nums[i] % 2:
            ans[i] = 1
        elif inbound(left) and nums[left] % 2 != nums[i] % 2:
            ans[i] = 1
        else:
            if inbound(right):
                graph[nums[i]] = graph[nums[right]]
                

    print(ans)


if __name__ == '__main__':
    solve_problem()