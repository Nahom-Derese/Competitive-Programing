# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted([num for num in nums if num > 0])

        new_nums = []
        for i in range(len(nums)):
            if not new_nums or nums[i] != new_nums[-1]:
                new_nums.append(nums[i])

        i = 0
        for i in range(1, len(new_nums)+1):
            if i != new_nums[i-1]:
                return i
        return i+1
        