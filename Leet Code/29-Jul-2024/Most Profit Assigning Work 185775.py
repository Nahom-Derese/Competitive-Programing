# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        difficulty_profit = list(zip(difficulty, profit))
        difficulty_profit.sort()
        worker.sort()
        itr = ans = 0

        heap = []

        for ability in worker:
            while itr < len(difficulty) and difficulty_profit[itr][0] <= ability:
                dif, pro = difficulty_profit[itr]
                heappush(heap, (-pro, dif))
                itr+=1
            if heap:
                ans += -heap[0][0]

        return ans
