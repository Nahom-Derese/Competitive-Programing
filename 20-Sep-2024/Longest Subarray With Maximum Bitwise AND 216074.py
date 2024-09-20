# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        x = max(nums)
        
        r = ans = 0
        while r < len(nums):
            count = 0
            while r < len(nums) and nums[r] == x:
                count += 1
                r+=1
            ans = max(ans, count)
            r+=1

        return ans