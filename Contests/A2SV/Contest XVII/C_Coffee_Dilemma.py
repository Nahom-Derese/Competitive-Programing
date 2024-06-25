n = int(input())

nums = [int(i) for i in input().split()]

def dp(idx, summ):
    if idx == len(nums):
        return 0
    if summ < 0:
        return 0

    if nums[idx] < 0:
        return max(1 + dp(idx+1, summ + nums[idx]), dp(idx+1, summ))
    
    return 1 + dp(idx+1, summ + nums[idx])

print(dp(0,0))