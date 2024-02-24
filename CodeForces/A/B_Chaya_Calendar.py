from math import ceil

for _ in range(int(input())):
    n = int(input())
    nums = [int(i) for i in input().split()]
    
    ans = nums[0]
    for i in nums[1:]:
        if ans < i:
            ans=i
        else:
            m = ceil((ans+1) / i)
            ans = i * m
    print(ans)
