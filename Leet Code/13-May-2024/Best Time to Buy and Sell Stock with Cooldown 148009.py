# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        count = 0
        mem = {}
        def solve(idx, bought):
            nonlocal count
            count += 1
            if idx >= len(prices):
                return 0

            state = (idx, bought)

            if state not in mem:
                if bought:
                    mem[state] = max(
                    solve(idx+2, False) + prices[idx],
                    solve(idx+1, bought)
                )
                else:
                    mem[state] = max(
                        solve(idx+1, True) - prices[idx],
                        solve(idx+1, False)
                    )
            return mem[state]
        
        x = solve(0, False)
        print(count)
        return x