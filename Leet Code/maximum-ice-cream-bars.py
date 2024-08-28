class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        print(sum(costs))
        ans = 0
        while coins >= costs[0] and ans < len(costs):
            coins-=costs[ans]

            if coins >= 0:
                ans+=1
        return ans