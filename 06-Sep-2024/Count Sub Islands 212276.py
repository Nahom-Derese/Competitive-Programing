# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        N, M = len(grid1), len(grid1[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(row, col):
            return (0 <= row < N and 0 <= col < M)
        
        def isIsland(row, col):
            return bool(grid2[row][col])

        
        def neighbours(row, col):
            for _row, _col in directions:
                new_row = row + _row
                new_col = col + _col
                if inbound(new_row, new_col) and isIsland(new_row, new_col):
                    yield (new_row, new_col)
            
        
        def bfs(row, col):
            res = 1
            queue = deque([])

            if not grid1[row][col]:
                res = 0
            
            if grid2[row][col] == 1:
                grid2[row][col] = 2
                queue = deque([(row, col)])

            else:
                return 0


            while queue:
                new_row, new_col = queue.popleft()

                for neighbour in neighbours(new_row, new_col):
                    next_row, next_col = neighbour
                    if not grid1[next_row][next_col]:
                        res = 0
                    if grid2[next_row][next_col] != 2:
                        queue.append(neighbour)
                    grid2[next_row][next_col] = 2

            return res
                


        ans = 0

        for i in range(N):
            for j in range(M):
                ans += bfs(i, j)
                
        return ans