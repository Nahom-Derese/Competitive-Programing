# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution(object):
    def rob(self, nums):
        x = defaultdict(list)
        
        if len(nums) < 3:
            return max(nums)
        
        x[-3] = [-1]
        
        for i in range(-4, -len(nums)-1, -1):
            x[i].extend(x[i+1])
            x[i].append(i+2)
        
        @cache
        def rec(n):
            res = nums[n]
            max_ = 0
            for i in x[n]:
                max_ = max(rec(i), max_)
            return res + max_
        
        return max(rec(-len(nums)), rec(-len(nums)+1))