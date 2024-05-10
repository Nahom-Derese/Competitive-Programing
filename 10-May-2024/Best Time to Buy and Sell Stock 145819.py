# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def findMax(idx):
            if idx == len(prices)-1:
                return prices[idx]
            
            return max(prices[idx], findMax(idx+1))

        ans = 0
        for i in range(len(prices)-1):
            ans = max( -prices[i] + findMax(i+1) , ans)
        
        return ans