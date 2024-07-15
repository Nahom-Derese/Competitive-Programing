def solve():    
    n, k = map(int, input().split())
    nums = [int(i) for i in input().split()]
   
    
    def helper(max_val):

        for i in range(n):

            cost = 0
            cur_val = max_val
            for j in range(i, n):
                
                if nums[j] < cur_val and j == n - 1:
                    cost = k + 1
                    break
                
                if nums[j] >= cur_val:
                    break

                cost += cur_val - nums[j]
                next_val = max(cur_val - 1, 0)
                cur_val = next_val

            if cost <= k:
                return True

        return False
    
    low, high = max(nums), max(nums) + min(n,k)
    while low <= high:
        mid =  low + (high - low) // 2
        if helper(mid):
            low = mid + 1
        else:
            high = mid - 1
    
    return high

for _ in range(int(input())):
    print(solve())

