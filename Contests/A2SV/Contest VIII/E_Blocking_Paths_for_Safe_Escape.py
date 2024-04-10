import sys
from collections import *
from itertools import *
from math import *
from collections import deque

grid = []
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
BadGuys = set()
GoodGuys = set()
EscapingGoodGuys = set()
EscapingBadGuys = set()

def inbound(row, col):
    return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

def escapable(row, col):
    if inbound(row, col):
        if grid[row][col] == "G":
            EscapingGoodGuys.add((row, col))
        if grid[row][col] == "B":
            EscapingBadGuys.add((row, col))
        return grid[row][col] != "#" 

def dfs_neighbour(row, col):
    res = []
    for row_change, col_change in directions:
        new_row = row + row_change
        new_col = col + col_change
        if escapable(new_row, new_col):
            res.append((new_row, new_col))
    
    return res

def dfs(row, col):
    
    queue = deque([(row, col)])

    grid[row][col] = ">"

    while queue:
        row, col = queue.popleft()

        for neighbour in dfs_neighbour(row, col):
            next_row , next_col = neighbour 
            if grid[next_row][next_col] != ">":
                queue.append(neighbour)
                grid[next_row][next_col] = ">"
        
def neighbours(row, col):
    res = []
    for _row, _col in directions:
        new_row = row + _row
        new_col = col + _col
        if inbound(new_row, new_col):
            res.append((new_row, new_col))
    return res

def solve():
    if not GoodGuys:
        return True
    
    bad_neighbours = [neighbours(*i) for i in BadGuys]
    bad_neighbours = list(chain.from_iterable(bad_neighbours))

    
    for n in bad_neighbours:
        if n in GoodGuys:
            return False
        else:
            row, col = n
            if grid[row][col] == ".":
                grid[row][col] = '#'

    door = (len(grid)-1, len(grid[0])-1)
    if grid[door[0]][door[1]] == ".":
        dfs(*door)
    else:
        return False
    return not EscapingBadGuys and len(GoodGuys) == len(EscapingGoodGuys)

for i in range(int(input())):
    m, n = [int(i) for i in sys.stdin.readline().split()]
    
    grid = []
    
    for i in range(m):
        s = sys.stdin.readline().strip()
        grid.append(list(s))

    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "B":
                BadGuys.add((i,j))
            if grid[i][j] == "G":
                GoodGuys.add((i,j))

    
    print("Yes") if solve() else print("No")

    # for i in grid:
    #     print("".join(i))


    BadGuys.clear()
    GoodGuys.clear()
    EscapingBadGuys.clear()
    EscapingGoodGuys.clear()