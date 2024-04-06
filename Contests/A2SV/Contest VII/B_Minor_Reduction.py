import sys
from collections import *
from itertools import *
from math import *

def solve(n):
    ans = 0
    for i in range(1, len(n)):
        current = str(int(n[i-1]) + int(n[i]))
        curr = n.copy()
        if len(current) > 1:
            curr[i] = current[1]
            curr[i-1] = current[0]
        else:
            curr[i] = current[0]
            curr.pop(i-1)

        ans = max(ans, int("".join(curr)))
        
    return ans


for i in range(int(input())):
    n = list(sys.stdin.readline().strip())
    
    print(solve(n))
            