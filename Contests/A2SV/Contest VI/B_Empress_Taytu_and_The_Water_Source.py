import sys
from math import ceil

def valid(demand, wagon_time, wagon_size , time_constraint):
    time = 0
    for i in range(len(demand)):
        time+= (ceil(demand[i]/wagon_size)) * wagon_time[i]
    return time <= time_constraint


def binary_search(demand, wagon_time, left, right, time_constraint):
    while left <= right:
        mid = left + (right - left) // 2
        if valid(demand, wagon_time, mid, k):
            right = mid - 1
        else:
            left = mid + 1
    return left


for i in range(int(input())):
    n, k = list(map(int, sys.stdin.readline().strip().split()))
    
    demand = list(map(int, sys.stdin.readline().strip().split()))
    wagon_time = list(map(int, sys.stdin.readline().strip().split()))
    
    ans = binary_search(demand, wagon_time, 1, max(demand), k)
    if ans > max(demand):
        print(-1)
    else:
        print(ans)
    

