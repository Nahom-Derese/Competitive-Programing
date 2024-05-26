n = int(input())

nums = [int(i) for i in input().split()]

r = 1

ans = 0
while r < len(nums):
    count = 0
    while r < len(nums) and nums[r-1] < nums[r]:
        count+=1
        r+=1
    ans = max(ans, count)
    r+=1

print(ans+1)