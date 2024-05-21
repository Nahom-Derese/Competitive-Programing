# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        @cache
        def dp(idx, bought, _try):
            if idx >= len(prices) or _try == 0:
                return 0
            
            if not bought:
                return max(
                    -prices[idx] + dp(idx+1, True, _try),
                    dp(idx+1, False, _try)
                )

            return max(
                dp(idx+1, False, _try-1) + prices[idx],
                dp(idx+1, True, _try)
            )
            
        return dp(0, False, 2)

