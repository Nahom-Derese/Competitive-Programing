def helper(n, nums):
    res = 0
    for i in nums:
        if i < n:
           res += (n-i)
    
    return res


def solve():
    n,target = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]

    left, right , best = 1, 10**10, float("-inf")

    while left <= right:
        mid = left + (right - left) // 2
        
        if helper(mid, nums) <= target:
            left = mid + 1
            best=mid
        else:
            right = mid - 1
    return best
    
for _ in range(int(input())):
    print(solve())
