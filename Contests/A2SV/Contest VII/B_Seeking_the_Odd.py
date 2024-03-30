import sys
from collections import *
from itertools import *
from math import *

def pow_two(n):
    return n & (n - 1) == 0


for i in range(int(input())):
    num = int(sys.stdin.readline())
    
    if not pow_two(num):
        print("YES")
    else:
        print("NO")