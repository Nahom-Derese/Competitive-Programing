import sys
from collections import *
from itertools import *
from math import *

grid = []
directions = [(-1, -1), (1, 1), (-1, 1), (1,-1)]

def inbound(row, col):
    global grid
    return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

def WhiteOrBlack(row, col):
    if (row+col)%2 == 0:
        return "W"
    return "B"

def neighbours(row, col):
    global directions
    res = []
    for coo in directions:
        row_change, col_change = coo
        
        new_row = row+row_change
        new_col = col+col_change
        
        while inbound(new_row, new_col) and grid[new_row][new_col] != "#":
            if grid[new_row][new_col] != ">":
                yield (new_row, new_col)
        
            new_row+=row_change
            new_col+=col_change
            

def bfs(row, col, target):
    global grid
    
    queue = deque([(row, col)])
    level = 1

    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            row, col = queue.popleft()
            for new_row, new_col in neighbours(row, col):
                # if grid[new_row][new_col] != ">":
                if (new_row, new_col) == target:
                    return level
                grid[new_row][new_col] = ">"
                queue.append((new_row, new_col))

        level+=1

    return -1


def solve_problem():
    global grid
    n = int(sys.stdin.readline().strip())
    
    sourceX, sourceY = [int(i) for i in sys.stdin.readline().split()]
    destX, destY = [int(i) for i in sys.stdin.readline().split()]

    if (sourceX, sourceY) == (destX, destY):
        return 0

    for _ in range(n):
        grid.append(list(input()))

    if WhiteOrBlack(sourceX-1, sourceY-1) != WhiteOrBlack(destX-1, destY-1) or grid[destX-1][destY-1] == "#":
        print(-1)
        return

    print(bfs(sourceX-1, sourceY-1, (destX-1, destY-1)))



    

if __name__ == '__main__':
    solve_problem()









def topological_sort(graph):
    indegree = [0] * len(graph)
    for neighbors in graph.values():
        for neighbor in neighbors:
            indegree[neighbor] += 1
    queue = deque([node for node in range(len(graph)) if indegree[node] == 0])
    res = []
    while queue:
        node = queue.popleft()
        res.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return res
