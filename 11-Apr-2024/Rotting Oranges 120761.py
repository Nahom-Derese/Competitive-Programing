# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def inBoundOrange(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0])) and grid[row][col]
        
        def neighbours(row, col):
            nonlocal visited
            nonlocal directions
            res = []
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if inBoundOrange(new_row, new_col):
                    res.append((new_row, new_col))
            return res

        rottenList = []
        empty_cells = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                empty_cells += grid[i][j] == 0
                if grid[i][j] == 2:
                    rottenList.append((i,j))
        oranges = (len(grid) * len(grid[0])) - empty_cells

        def bfs():
            nonlocal visited
            visited.update(rottenList)
            queue = deque(rottenList)
            time = 0
            while queue and len(visited) != oranges:
                length = len(queue)
                time+=1
                for _ in range(length):
                    x = queue.popleft()

                    for orange in neighbours(*x):
                        if orange not in visited:
                            visited.add(orange)
                            queue.append(orange)
            
            if len(visited) != oranges:
                return -1
            return time

        return bfs()