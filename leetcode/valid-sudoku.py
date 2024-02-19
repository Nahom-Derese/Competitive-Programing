class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for i in range(len(board)):
            freq = Counter(board[i])
            for i in freq:
                if i != '.' and freq[i] > 1:
                    return False
        
        # check col
        for i in range(len(board)):
            freq = Counter(list(zip(*board))[i])
            for i in freq:
                if i != '.' and freq[i] > 1:
                    return False
        
     
        # check 3x3 grid
        for i in range(0,9,3):
            for j in range(0,9,3):
                unique = set()
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        # print(board[k][l])
                        if board[k][l] != "." and board[k][l] in unique:
                            return False
                        unique.add(board[k][l])

        return True