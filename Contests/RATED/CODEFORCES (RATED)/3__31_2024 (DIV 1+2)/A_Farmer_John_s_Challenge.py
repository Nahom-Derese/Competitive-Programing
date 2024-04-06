import sys
from collections import *
from itertools import *
from math import *


for i in range(int(input())):
    n, k = [int(i) for i in sys.stdin.readline().split()]
    
    
    if n == k:
        print(*[1]*n)
    else:
        if k == 1:
            print(*list(range(1,n+1)))
        else:
            print(-1)