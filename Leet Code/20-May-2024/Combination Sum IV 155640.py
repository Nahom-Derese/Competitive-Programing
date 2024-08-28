# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        

        @cache
        def dp(summ):
            if summ == target:
                return 1

            if summ > target:
                return 0
            
            res = 0
            for num in nums:
                res += dp(summ + num)
            
            return res

        return dp(0)