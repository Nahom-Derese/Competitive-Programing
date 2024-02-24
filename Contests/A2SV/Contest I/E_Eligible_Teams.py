from math import ceil, floor
 
def answer(nums, limit, n):
    teams = 0
    l = -1
    r = 0
    ans = 0
    while r < n:
        if nums[r] * (r-l) >= limit:
            ans+=1
            l=r    
        r+=1
    return ans
    
for i in range(int(input())):
    n, l = map(int, input().split())
 
    nums = list(map(int, input().split()))
    
    nums.sort(reverse=True)
 
    print(answer(nums, l, n))
