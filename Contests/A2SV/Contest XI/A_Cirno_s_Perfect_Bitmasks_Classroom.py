import sys
from collections import *
from itertools import *
from math import *


for i in range(int(input())):
    n = int(sys.stdin.readline().strip())
    
    if n == 1:
        print(3)
    else:
        original = n
        ans = x = 0
        while n&1 == 0:
            n >>= 1
            x+=1
        
        if original ^ (1 << x) == 0:
            ans += 1
        
        print(ans+(1<<x))
