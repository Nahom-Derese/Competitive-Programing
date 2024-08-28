# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        visited = set()
        board.reverse()


        def findCoordinate(cell):
            row = (cell-1)//n
            col = (cell-1)%n

            if row % 2:
                col = n - 1 - col
            
            return (row, col)


        def neighbours(cell):
            res = []
            for i in range(cell+1, min(cell+7, (n*n)+1)):
                row, col = findCoordinate(i)
                
                if board[row][col] != -1:
                    res.append(board[row][col])
                else:
                    res.append(i)
            return res

        def bfs():

            queue = deque([1])
            roll = 0

            while queue:
                boundary = len(queue)
                
                for _ in range(boundary):
                    cell = queue.popleft()
                    print(cell, end=" ")
                    if cell == n ** 2:
                        return roll
                    
                    next_round = neighbours(cell)
                    for i in next_round:
                        if i not in visited:
                            visited.add(i)
                            queue.append(i)
                    
                roll += 1

            return -1
        
        return bfs()