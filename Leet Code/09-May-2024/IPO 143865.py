# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        profits_heap = []
        capital_heap = [(capital[i], -profits[i])  for i in range(len(profits))]

        heapify(capital_heap)
        
        for i in range(k):
            while capital_heap and capital_heap[0][0] <= w:
                heappush(profits_heap, heappop(capital_heap)[::-1])

            if profits_heap:
                w += -heappop(profits_heap)[0]

        return w