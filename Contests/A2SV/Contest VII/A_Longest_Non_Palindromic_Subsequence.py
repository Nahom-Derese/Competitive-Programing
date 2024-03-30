import sys
from collections import *
from itertools import *
from math import *

def solve(s):
    if len(set(s)) == 1:
        print(-1)
    else:
        print(len(s)-1)

for i in range(int(input())):
    s = sys.stdin.readline().strip()

    solve(s)