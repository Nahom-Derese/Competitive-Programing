import sys
from collections import *
from itertools import *
from math import *


n, m = [int(i) for i in sys.stdin.readline().split()]

def check(flag):
    prev = -1
    for i in flag:
        if len(i) > 1:
            return False
        elif prev == i:
            return False
        prev = i
    return True

flag = []
for i in range(n):
    flag.append(set(sys.stdin.readline().strip()))

if check(flag):
    print("YES")
else:
    print("NO")