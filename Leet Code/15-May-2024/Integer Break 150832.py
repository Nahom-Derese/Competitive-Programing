# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n-1
        
        ans = 0

        @cache
        def dp(summ, mult):
            nonlocal ans
            if summ > n:
                return 
            if summ == n:
                ans = mult
                return 
            
            dp(summ + 2, mult * 2)
            dp(summ + 3, mult * 3)
        
        dp(0, 1)
        return ans