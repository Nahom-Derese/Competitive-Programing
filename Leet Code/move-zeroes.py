class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = r = 0

        while r < len(nums):
            if nums[l]:
                l += 1
            elif nums[r]:
                nums[l], nums[r] = nums[r], nums[l] 
                l += 1
            r+=1