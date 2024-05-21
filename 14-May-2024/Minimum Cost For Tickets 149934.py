# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        consecutive_days = [1,7,30]

        @cache
        def dp(day):
            if day > days[-1]:
                return 0
            
            idx = bisect_left(days, day)
            day = days[idx]
            
            ans = float("inf")
            for i in range(len(costs)):
                ans = min(ans, costs[i] + dp(day + consecutive_days[i]))
            return ans

        return dp(days[0])