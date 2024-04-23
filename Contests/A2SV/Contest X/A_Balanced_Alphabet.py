import sys
from collections import *
from itertools import *
from math import *
from string import ascii_lowercase

for i in range(int(input())):
    n, k = [int(i) for i in sys.stdin.readline().split()]
    
    i = 0
    ans = ""
    while i != n:
        ans+=ascii_lowercase[i%k]
        i+=1
    print(ans)