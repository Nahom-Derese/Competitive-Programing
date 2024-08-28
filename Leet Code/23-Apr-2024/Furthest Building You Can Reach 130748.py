# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []

        for i in range(1, len(heights)):
            jump = heights[i] - heights[i-1]

            if jump <= 0:
                continue
            
            if ladders:
                ladders-=1
                heappush(heap, jump)
            
            else:
                min_ladder_used = heappushpop(heap, jump)
                if min_ladder_used > bricks:
                    return i -1 
                
                bricks -= min_ladder_used

        return len(heights)-1