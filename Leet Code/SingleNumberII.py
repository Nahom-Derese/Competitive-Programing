from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        for i in nums:
            a = dict.get(i,0) + 1
            dict[i] = a
        for i in dict:
            if dict.get(i) == 1:
                return i


# print(Solution.singleNumber(Solution,[0,1,0,1,0,1,99]))