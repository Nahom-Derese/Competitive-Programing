import sys
from collections import deque

def prefix_sum(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        prefix[i] = prefix[i - 1] + ord(arr[i - 1])
    return prefix


for i in range(int(input())):
    n, m = list(map(int, sys.stdin.readline().strip().split()))
    s = sys.stdin.readline().strip()
    search = sys.stdin.readline().strip()

    target = sum(list(map(ord, search)))
    

    l = cur_sum = 0
    r = m-1
    found = False

    
    while r < n:
        cur_sum = p_sum[r+1] - p_sum[l]
        
        
        if cur_sum == target:
            found = True
            print("YES")
            break

        l+=1
        r+=1

    if not found:
        print("NO")
    