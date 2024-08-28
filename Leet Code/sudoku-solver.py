class Solution:
    def validate(self, board: List[List[str]], x: int, y: int) -> bool:
        current_square_x = (x//3)*3
        current_square_y = (y//3)*3
        unique = set()
        for k in range(current_square_x,current_square_x+3):
            for l in range(current_square_y,current_square_y+3):
                if board[k][l] != "." and board[k][l] in unique:
                    return False
                unique.add(board[k][l])
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        candidates = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    candidates.append([i, j])
        
        row = {
            i: Counter(board[i]) for i in range(9)
        }
        cc = list(zip(*board))
        column = {
            i: Counter(cc[i]) for i in range(9)
        }

        def solve(idx):
            if idx == len(candidates):
                return True

            x, y = candidates[idx]
            for i in range(1, 10):
                if  row[x][str(i)] == 0 and column[y][str(i)] == 0:
                    board[x][y] = str(i)
                    row[x][str(i)] += 1
                    column[y][str(i)] += 1
                    if not self.validate(board, x, y):
                        board[x][y] = "."
                        row[x][str(i)] -= 1
                        column[y][str(i)] -= 1
                    elif solve(idx+1):
                        return True
                    else:
                        board[x][y] = "."
                        row[x][str(i)] -= 1
                        column[y][str(i)] -= 1

        solve(0)
