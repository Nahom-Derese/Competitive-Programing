from sys import stdin
from collections import Counter

input = stdin.readline

for i in range(int(input())):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))

    u = Counter(nums)
    t = []

    for (k,l) in u.items():
        if l >= m:
            t.append(k)
        
    left = 0
    right = 0
    window_size = 0
    a,b = 0,0
    t.sort()
    
    absolute_difference = 0
    left = 0
    right = 1
    if len(t) == 0:
        print(-1)
        continue
    a,b = t[left], t[left]
    while right < len(t):
        if right != left and t[right] - t[right-1] != 1:
            left = right
            continue

        current_difference = t[right] - t[left]
        if current_difference > absolute_difference:
            absolute_difference = current_difference
            a,b = t[left], t[right]
        
        right += 1
    print(a,b)