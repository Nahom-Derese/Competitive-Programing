import sys
from math import ceil, inf

def solve(health, power):

    stack = [[inf, power[0]]]
    ans = 0
    for i in range(1, len(health)):
        duration = 0
        
        while health[i] - (stack[-1][0] - duration)*stack[-1][1] > 0:
            t, p = stack.pop()

            health[i] -= (t-duration)*p
            duration += (t-duration)

        duration += ceil(health[i] / stack[-1][1])
        ans = max(ans, duration)
        stack.append([duration, power[i]])
    
    
    return ans
    

for i in range(int(input())):
    n = int(sys.stdin.readline().strip())
    
    health = list(map(int, sys.stdin.readline().strip().split()))
    power = list(map(int, sys.stdin.readline().strip().split()))

    print(solve(health, power))