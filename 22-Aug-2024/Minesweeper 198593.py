# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        n = len(board)
        m = len(board[0])
        visited = [[False] * m for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]

        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m


        def neighbors(row, col):
            res = []
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if inbound(new_row, new_col):
                    res.append((new_row, new_col))

            return res
            
        def dfs(row, col):
            if board[row][col] == "M":
                board[row][col] = "X"
                return

            visited[row][col] = True
            neighbours = neighbors(row, col)
            
            mines = 0
            for new_row, new_col in neighbours:
                mines += board[new_row][new_col] == 'M'
            
            if mines:
                board[row][col] = str(mines)
                return 
            
            if board[row][col] == "E":
                board[row][col] = "B"
            
            for new_row, new_col in neighbours:
                if not visited[new_row][new_col]:
                    dfs(new_row, new_col)

        dfs(*click)

        return board