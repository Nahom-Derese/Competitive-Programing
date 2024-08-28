class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        ans = len(nums)
        current = r = l = 0

        while r < len(nums):
            current += nums[r]

            while current >= target:
                ans = min(ans, r-l+1)
                current -= nums[l]
                l+=1
            
            print(current)
            r+=1
        
        if ans == len(nums):
            if sum(nums) < target:
                return 0
        return ans