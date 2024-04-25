# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        ans = 0
        while coins >= costs[0] and ans < len(costs):
            coins-=costs[ans]

            if coins >= 0:
                ans+=1
        return ans