import sys
from collections import *
from math import *

def cycleLength(cycle):
    length = len(cycle)
    for i in range(1, length + 1):
        if length % i == 0:
            pattern = cycle[:i]
            if all(cycle[j:j+i] == pattern for j in range(0, length, i)):
                return i
    return length

for i in range(int(sys.stdin.readline().strip())):
    n = int(sys.stdin.readline().strip())
    string = list(sys.stdin.readline().strip())
    nums = [int(i) for i in sys.stdin.readline().split()]
    
    visited = set()
    cycles = []
    for i in range(n):
        x = nums[i]
        count = 0
        cycle = []
        while (x not in visited):
            visited.add(x)
            cycle.append(string[x-1])
            count+=1
            x = nums[x-1]
            if x == i+1:
                visited.add(x)
                cycle.append(string[x-1])
                break
        if count:
            cycles.append(cycle)
    
    print(lcm(*map(cycleLength, cycles)))