ans = []

for i in range(int(input())):
    stacks = int(input())
    heights = list(map(int, input().split()))
    
    r = 0
    for k in range(stacks):
        heights[k] = r + heights[k]
        if heights[k] >= k:
            r = heights[k] - k
        heights[k] -= r

    for j in range(stacks-1):
        if heights[j] >= heights[j+1]:
            ans.append("NO")
            break
    else:
        ans.append("YES")

for i in ans:
    print(i)