# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        y = list(zip(efficiency, speed))
        x = sorted(y, reverse=True)
        
        heap = []
        speed = ans = 0
        for i in range(len(x)):
            if len(heap) == k:
                speed -= heappop(heap)
            speed += x[i][1]
            heappush(heap, x[i][1])
            ans = max(x[i][0] * speed, ans)

        return ans % (10 ** 9 + 7)