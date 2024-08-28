# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        

        @cache
        def dp(l, r, Alice):
            if r <= l:
                return 0

            if Alice:
                return max(piles[r] + dp(l, r-1, False), piles[l] + dp(l+1, r, False))
            else:
                return max(dp(l, r-1, True) - piles[r] , dp(l+1, r, True) - piles[l])

        return dp(0, len(piles)-1, True) > 0