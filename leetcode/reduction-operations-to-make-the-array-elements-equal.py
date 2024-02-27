class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        nums.sort()
        r = 1
        ans = 0
        while r < len(nums):
            while r < len(nums) and nums[r-1] == nums[r]:
                r+=1
            ans+=len(nums) - r
            r+=1
        return ans