# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        ans = [[0 for i in range(len(mat[0]))] for _ in range(len(mat))]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def inbound(row, col):
            return (0 <= row < len(mat) and 0 <= col < len(mat[0]))

        def neighbour(row, col):
            for r_change, c_change in directions:
                new_col = col + c_change
                new_row = row + r_change
                if inbound(new_row, new_col) and (new_row, new_col) not in visited:  
                    yield (new_row, new_col)
        
        def bfs(zeroes):
            queue = deque(zeroes)
            while queue:
                boundary = len(queue)
                
                for _ in range(boundary):
                    cell, level = queue.popleft()
                    row, col = cell
                    
                    if mat[row][col]:
                        ans[row][col] = -(min(ans[row][col], -level))

                    for neigh in neighbour(row, col):
                        if neigh not in visited:
                            visited.add(neigh)
                            queue.append((neigh,level+1))


        zeroes = []
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if not mat[row][col]:
                    zeroes.append([(row, col),0])
        bfs(zeroes)
        return ans