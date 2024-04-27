import sys
from collections import *
from itertools import *
from math import *

def solve_problem(s):
    
    if len(s) % 2:
        return "NO"
    x = s[:(len(s)//2)]
    y = s[len(s)//2:]

    if x == y:
        return "YES"
    return "NO"

if __name__ == '__main__':

    for _ in range(int(input())):
        s = sys.stdin.readline().strip()
        
        print(solve_problem(s))
    