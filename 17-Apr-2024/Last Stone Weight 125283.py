# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapify(stones)
        while len(stones) > 1:
            x1 = heappop(stones)
            x2 = heappop(stones)
            diff = x1-x2
            if diff:
                heappush(stones, diff)
            
        if stones: return -stones[0]
        return 0