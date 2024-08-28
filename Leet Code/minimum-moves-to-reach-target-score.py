class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        while maxDoubles and target > 1:
            if target % 2 == 0:
                ans+=1
            else:
                ans+=2
            maxDoubles-=1
            target = target//2
        
        return ans + target-1