from cmath import inf
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        arr = nums[:k]
        res = arr[-1] - arr[0]
        
        for i in range(k, len(nums)):
            arr.pop(0)
            arr.append(nums[i])
            res = min(res, arr[-1] - arr[0])
            
        return res
