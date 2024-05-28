H, W = [int(i) for i in input().split()]
matrix = [list(input()) for _ in range(H)]
dp = [[0 for i in range(W+1)] for _ in range(H+1)]
dp[0][1] = 1

directions = [(0, -1), (-1, 0)]

def inbound(row, col):
    return 0 <= row < H+1 and 0 <= col < W+1

def parents(row, col):
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if inbound(new_row, new_col):
            yield new_row, new_col

for row in range(1, H+1):
    for col in range(1, W+1):
        if matrix[row-1][col-1] == '.':
            for new_row, new_col in parents(row, col):
                dp[row][col] += dp[new_row][new_col]
                dp[row][col] %= (10**9 + 7)


print(dp[H][W])