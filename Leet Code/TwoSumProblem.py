from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         dict = {}
#         for k in range(len(nums)):
#             i = nums[k]
#             if(i in dict):
#                 return [dict[i], k]
#             dict[target - i] = nums.index(i)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]
           
            if remaining in seen:
               return [i, seen[remaining]]
            
            seen[value] = i

print(Solution().twoSum([2,7,11,15], 9))