# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ % 2:
            return False
        
        half = summ // 2
        
        @cache
        def dp(idx, tot):
            if idx == len(nums) or tot < 0:
                return 0

            if tot == 0:
                return 1
            
            return dp(idx+1, tot - nums[idx]) or dp(idx+1, tot)

        return bool(dp(0, half))