visited = [[False] * m for _ in range(n)]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def inbound(row, col):
    return 0 <= row < n and 0 <= col < m

def neighbors(row, col):
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if inbound(new_row, new_col):
            yield new_row, new_col

def dfs(row, col):
    visited[row][col] = True
    for new_row, new_col in neighbors(row, col):
        if not visited[new_row][new_col]:
            dfs(new_row, new_col)

