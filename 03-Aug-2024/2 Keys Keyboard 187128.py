# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
        @lru_cache(None)
        def dp(ops, curr, saved):
            if curr == n: return ops
            if curr > n: return inf
            if curr == saved: return dp(ops + 1, curr + saved, saved)
            if saved == 0: return dp(ops + 1, curr, curr)
            return min(dp(ops + 1, curr + saved, saved), dp(ops + 1, curr, curr))
        return dp(0, 1, 0)    
        