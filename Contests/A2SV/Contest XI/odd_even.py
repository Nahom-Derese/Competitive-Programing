import sys
from collections import *
from itertools import *
from math import *


for i in range(int(input())):
    n = int(sys.stdin.readline().strip())
    nums = [int(i) for i in sys.stdin.readline().split()]
    
    sorted_nums = sorted(nums)

    for i in range(n):
        num = nums[i]
        num_s = sorted_nums[i]

        if num % 2 != num_s % 2:
            print("NO")
            break
    else:
        print("YES")