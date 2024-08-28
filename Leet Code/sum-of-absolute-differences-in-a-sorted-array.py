class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = list(accumulate(nums))
        suffix = list(accumulate(nums[::-1]))[::-1]
        length = len(nums) - 1

        return [abs((i * nums[i]) - (prefix[i] - nums[i])) + abs((suffix[i] - nums[i]) - ((length-i) * nums[i])) for i in range(len(nums))]