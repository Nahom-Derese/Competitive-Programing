class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for k in range(len(nums)):
            i = nums[k]
            if(i in dict):
                return [dict[i], k]
            dict[target - i] = nums.index(i)