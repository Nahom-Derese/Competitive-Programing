# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def dp(idx, tot):
            if idx == len(coins) or tot > amount:
                return 0
            if tot == amount:
                return 1

            return  dp(idx, tot + coins[idx]) + dp(idx+1, tot)
        
        return dp(0, 0)