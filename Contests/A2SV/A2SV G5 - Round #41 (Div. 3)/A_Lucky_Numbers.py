n, k = [int(i) for i in input().split()]

nums = [int(i) for i in input().split()]
ans = 0

for num in nums:
    count = 0
    for char in str(num):
        if char == "4" or char == "7":
            count += 1
    if count <= k:
        ans+=1

print(ans)