# Problem: Minimum Increment to Make Array Unique - https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        r = ans = 0
        
        prev = -1
        while r < len(nums):

            if prev >= nums[r]:
                ans += prev+1 - nums[r]
                nums[r] = prev+1

            prev = nums[r]
            r+=1
        
        return ans