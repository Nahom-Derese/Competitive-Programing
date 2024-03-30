import sys
from collections import *
from itertools import *
from math import *

def divide(x):
    while x%2 == 0:
        x//=2
    while x%3 == 0:
        x//=3
    return x
    
n = int(sys.stdin.readline().strip())

nums = [int(i) for i in sys.stdin.readline().split()]

if len(set(map(divide, nums))) == 1:
    print("Yes")
else:
    print("No")