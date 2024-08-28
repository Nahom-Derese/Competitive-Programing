grid = []

for _ in range(int(input())):
    grid.append([int(i) for i in input().split()])
    
transpose = list(zip(*grid))

def searchSum(a, b, s):
    for i in a:
        for j in b:
            if i+j == s:
                return True
    return False

for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] != 1:
            col = list(transpose[j] )
            row = grid[i][:]


            if not searchSum(col, row, grid[i][j]):
                print("No")
                exit()

print("Yes")