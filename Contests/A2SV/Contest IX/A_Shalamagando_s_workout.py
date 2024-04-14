import sys
from collections import *
from itertools import *
from math import *

def solve_problem():
    n = int(sys.stdin.readline().strip())
    
    exercise = [int(i) for i in sys.stdin.readline().split()]
    
    exe = [0,0,0]

    for i in range(0,len(exercise),3):
        exe[0]+=exercise[i]
    
    for i in range(min(1, len(exercise)), len(exercise),3):
        exe[1]+=exercise[i]
    
    for i in range(min(2, len(exercise)), len(exercise),3):
        exe[2]+=exercise[i]

    x = exe.index(max(exe))

    if x==0:
        return "chest"
    if x==1:
        return "biceps"
    else:
        return "back"
        
if __name__ == '__main__':
    print(solve_problem())