# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(1,1), (1,-1), (-1,-1), (-1,1), (0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

        def neighbours(row, col, hop):
            res = []
            for _row, _col in directions:
                new_row = row + _row
                new_col = col + _col
                if inbound(new_row, new_col):
                    res.append((new_row, new_col, hop+1))
            return res
        
        def bfs(row, col):
            if grid[row][col]:
                return -1

            queue = deque([(row, col, 1)])
            while queue:
                new_row, new_col, hop = queue.popleft()
                
                
                if (new_row, new_col) == (len(grid)-1, len(grid[0])-1):
                    return hop

                
                for neighbour in neighbours(new_row, new_col, hop):
                    if grid[neighbour[0]][neighbour[1]] == 0:
                        queue.append(neighbour)
                        grid[neighbour[0]][neighbour[1]] = ">"
                

            return -1

        return bfs(0,0)

        
                