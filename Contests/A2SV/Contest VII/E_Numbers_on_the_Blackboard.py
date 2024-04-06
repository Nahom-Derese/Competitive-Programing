import sys
from collections import *
from itertools import *
from math import *

def solve(nums):
  
    pos = neg = zeros = 0
    
    for i in nums:
        pos+=i>0
        neg+=i<0
        zeros+=i==0

    if zeros == len(nums):
        return 0

    if pos == len(nums) or neg == len(nums):
        gcf = gcd(*nums)
        ans = sum(map(lambda x:abs((x//gcf))-1, nums))
        return ans
    else:
        return -1


for i in range(int(input())):
    n,k = [int(i) for i in sys.stdin.readline().split()]
    
    nums = [int(i) - k for i in sys.stdin.readline().split()]

    print(solve(nums))