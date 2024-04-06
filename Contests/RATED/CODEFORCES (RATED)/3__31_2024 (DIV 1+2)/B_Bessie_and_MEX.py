import sys
from collections import *
from itertools import *
from math import *


for i in range(int(input())):
    n = int(sys.stdin.readline().strip())
    
    nums = [int(i) for i in sys.stdin.readline().split()]
    ans = deque()
    for i in range(-1,-len(nums)-1, -1):
        if nums[i] >= 0:
            n -= nums[i]
            ans.appendleft(n) 
        else:
            ans.appendleft(n-nums[i]) 

    print(*list(ans))
    