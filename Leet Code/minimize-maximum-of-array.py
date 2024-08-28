class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        min_ = nums[0]
        pre_sum = list(accumulate(nums))
        for i in range(1, len(nums)):
            if nums[i] > min_:
                min_ = max(ceil(pre_sum[i] / (i+1)), min_)
        return min_