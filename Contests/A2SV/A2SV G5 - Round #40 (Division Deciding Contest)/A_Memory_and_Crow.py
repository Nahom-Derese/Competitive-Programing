n = int(input())

nums = [int(i) for i in input().split()]
nums.append(0)

ans = []

for i in range(n):
    ans.append(nums[i] + nums[i+1])

print(*ans)