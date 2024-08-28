class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre_sum = [0] + list(accumulate(nums))
        suf_sum = list(accumulate(nums[::-1]))[::-1] + [0]

        for i in range(len(nums)):
            if pre_sum[i] == suf_sum[i+1]:
                return i
        return -1