# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(row, col):
            return (0 <= row < len(board) and 0 <= col < len(board[0]))

        def bfs(multi_source):
            queue = deque(multi_source)
            
            while queue:
                row, col = queue.popleft()
                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change
                    if inbound(new_row, new_col) and board[new_row][new_col] == "O" and (new_row, new_col) not in visited:
                        visited.add((new_row,new_col))
                        queue.append((new_row, new_col))

        zeros_1 = [0] * len(board) + [len(board[0])-1] * len(board)
        zeros_2 = [0] * len(board[0]) + [len(board)-1] * len(board[0])
        nums1 = list(range(len(board))) + list(range(len(board)))
        nums2 = list(range(len(board[0]))) + list(range(len(board[0])))

        multi_source = []
        for i,j in  list(zip(nums1, zeros_1)) + list(zip(zeros_2, nums2)):
            if board[i][j] == "O":
                multi_source.append((i,j))

        bfs(multi_source)

        for i in range(1, len(board)-1):
            for j in range(1, len(board[0])-1):
                if (i,j) not in visited:
                    board[i][j] = "X"