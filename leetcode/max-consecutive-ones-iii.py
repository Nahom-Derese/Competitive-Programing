class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        
        l = r = 0
        currentSum = 0
        while r < len(nums):
            currentSum+=nums[r]

            while r-l+1 - currentSum > k:
                currentSum-=nums[l]
                l+=1
            
            ans = max(ans, r-l+1)

            r+=1
        
        return ans