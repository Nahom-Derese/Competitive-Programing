i = int(input())
ans = 0
for _ in range(i):
    x, y = [int(u) for u in input().split()]
    if y-x > 1:
        ans+=1
    
print(ans)