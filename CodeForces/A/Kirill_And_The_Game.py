l, r, x, y, k = [int(i) for i in input().split()]

for cost in range(x, y+1):
    effectiveness = cost * k
    if l <= effectiveness <= r:
        print("YES")
        break
else:
    print("NO")
