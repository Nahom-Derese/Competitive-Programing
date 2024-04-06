import sys
from collections import *
from itertools import *
from math import *

a, b = [int(i) for i in sys.stdin.readline().split()]

for i in range(b):
    if a % 10 == 0:
        a //= 10
    else:
        a-=1

print(a)