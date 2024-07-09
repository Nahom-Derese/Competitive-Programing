# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: -x, stones))
        heapify(stones)
        while len(stones) > 1:
            x = heappop(stones) - heappop(stones)
            if x:
                heappush(stones, x)
        
        if stones:
            return -1 * stones[0]
        return 0