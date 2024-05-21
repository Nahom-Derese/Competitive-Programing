# directions = [(0,-1), (-1,0), (0,1), (1,0)]

# def inbound(row, col):
#     if row < 0 or row >= len(grid):
#         return False
#     if col < 0 or col >= len(grid[0]):
#         return False
#     return True

# def neighbours(row, col):
#     for dr, dc in directions:
#         r, c = row + dr, col + dc
#         if inbound(r, c) and grid[r][c] != '0':
#             yield r, c

# def dfs(row, col):
#     if grid[row][col] == '0':
#         return
#     grid[row][col] = '0'
#     for r, c in neighbours(row, col):
#         dfs(r, c)

    
def twos_complement(n):
    return ~n + 1

while True:
    x = input()
    if x == '':
        break
    print(bin(twos_complement(int(x))), bin(int(x)))

