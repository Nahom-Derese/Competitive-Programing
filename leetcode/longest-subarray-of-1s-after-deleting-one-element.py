class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0

        maxx = float("-inf")
        zeros = 0
        while right < len(nums):
            if nums[right] == 0:
                zeros+=1
            
            while zeros>1:
                if nums[left] == 0:
                    zeros-=1
                left+=1
            
            if zeros == 0:
                maxx = max(maxx, right-left)
            else:
                maxx = max(maxx, (right-left)+1 - zeros)

            right+=1

        
        return maxx