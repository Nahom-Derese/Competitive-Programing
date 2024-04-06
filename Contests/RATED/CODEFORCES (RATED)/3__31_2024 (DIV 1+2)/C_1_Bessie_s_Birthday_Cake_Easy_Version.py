import sys
from collections import *
from itertools import *
from math import *

for i in range(int(input())):
    n, x, y = [int(i) for i in sys.stdin.readline().split()]
    
    points = sorted([int(i) for i in sys.stdin.readline().split()])
    
    l = ans = 0
    r = len(points) - 1

