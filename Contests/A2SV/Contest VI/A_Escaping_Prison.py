import sys

for _ in range(int(input())):
    n, h = list(map(int, input().split()))
    
    tot = 0
    for _ in range(n):
        tot+=max(list(map(int, input().split())))
    
    if tot < h:
        print("NO")
    else:
        print("YES")