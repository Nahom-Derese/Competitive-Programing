n, q = map(int, input().split())
nums = list(map(int, input().split()))
pre_sum = [0,0]

for i in range(2,n):
    pre_sum.append(pre_sum[-1] + int(nums[i-2] >= nums[i-1] and nums[i-1] >= nums[i]))
    
for _ in range(q):
    l, r = map(int, input().split())
    
    if r == l:
        print(1)
        
    else:
        print((r - l + 1) - (pre_sum[r-1] - pre_sum[l]))