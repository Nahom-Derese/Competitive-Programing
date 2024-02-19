class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        x = sorted(nums)
        return list(map(lambda i: x.index(i), nums))