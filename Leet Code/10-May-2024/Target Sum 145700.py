# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
        @cache
        def rec(idx, summ=0):            
            if idx == len(nums):
                if summ == target:
                    return 1
                return 0

            ans = 0
            ans+=rec(idx+1, summ+nums[idx])
            ans+=rec(idx+1, summ-nums[idx])
            
            return ans

        return rec(0)