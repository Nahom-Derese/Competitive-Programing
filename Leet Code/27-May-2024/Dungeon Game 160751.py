# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])

        @cache
        def dp(i, j):

            if i == n - 1 and j == m - 1:
                if dungeon[i][j] >= 0:
                    return 1 
                else:
                    return -dungeon[i][j] + 1
            if i >= n or j >= m:
                return float("inf")
            
            
            res = dungeon[i][j] - min(
                dp(i + 1, j),
                dp(i, j + 1)
            )

            if res >= 0:
                return 1
            else: 
                return -res 

        return dp(0, 0)
        