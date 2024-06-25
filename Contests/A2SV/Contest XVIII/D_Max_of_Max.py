def solve():    
    n, k = map(int, input().split())
    nums = [int(i) for i in input().split()]
   
    
    def helper(mid):
        opp = 0
        for i in range(n - 1):
            if nums[i] < nums[i + 1] and nums[i] < mid:
                opp += mid - nums[i]
                if opp > k:
                    return False
        return True
    
    low, high = max(nums), max(nums) + k + 1
    while low <= high:
        mid =  low + (high - low) // 2
        if helper(mid):
            low = mid + 1
        else:
            high = mid - 1
    
    return high

for _ in range(int(input())):
    print(solve())

