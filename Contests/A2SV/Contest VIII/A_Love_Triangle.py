import sys
from collections import *
from itertools import *
from math import *


def solve_problem():
    n = int(sys.stdin.readline().strip())
    planes = [int(i) for i in sys.stdin.readline().split()]
    for i in range(len(planes)):
        x = planes[i] - 1
        visited = 1
        while x != i and visited < len(planes):
            x = planes[x] - 1
            visited+=1
        
        if x == i and visited == 3:
            print("YES")
            return
    else:
        print("NO")

if __name__ == '__main__':
    solve_problem()