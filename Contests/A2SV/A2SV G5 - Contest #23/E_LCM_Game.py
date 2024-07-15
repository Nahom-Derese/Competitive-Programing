from math import lcm
from itertools import combinations

def solve(n):
    max_lcm_value = 0
    
    for a, b, c in combinations(range(1, n+1), 3):
        current_lcm = lcm(a, b, c)
        if current_lcm > max_lcm_value:
            max_lcm_value = current_lcm
    return max_lcm_value

n = int(input())
print(solve(n))