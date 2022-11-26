from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in Solution.permutation(nums):
            ans.append(i)
        return ans


    def permutation(list: List[int]) -> List[int]:
        if len(list) == 0:
            return []
        if len(list) == 1:
            return [list]
        else:
            l = []
            for i in range(len(list)):
                x = list[i]
                xs = list[:i] + list[i+1:]
                for p in Solution.permutation(xs):
                    l.append([x] + p)
                
            return l
        
print(Solution.permute(Solution,[1,2,3]))