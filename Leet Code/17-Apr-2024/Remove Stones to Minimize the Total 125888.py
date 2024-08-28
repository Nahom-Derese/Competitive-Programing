# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-x for x in piles]
        heapify(piles)

        for i in range(k):
            removedPile = piles[0]
            heappushpop(piles, removedPile // 2)
        
        return sum([-x for x in piles])