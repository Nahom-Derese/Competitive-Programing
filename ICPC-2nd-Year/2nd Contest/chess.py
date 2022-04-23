drn = [
    [1, 2],
    [1, -2],
    [-1, 2],
    [-1, -2],

    [2, 1],
    [2, -1],
    [-2, 1],
    [-2, -1]
]
while True:
    row, col = [int(x) for x in input().split(' ')]
    if row == 0 and col == 0:
        break

    count = 0
    matrix = [[None for c in range(col)] for r in range(row)]
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == None:
                start = [i, j, 'N']
                stack = [start]

                while len(stack) > 0:
                    top = stack.pop()
                    if matrix[top[0]][top[1]] == 'X'  or matrix[top[0]][top[1]] == 'N': 
                        continue
                    
                    matrix[top[0]][top[1]] = top[2] 
                    if top[2] == 'N':
                        count += 1
                    sym = 'X' if top[2] == 'N' else 'N'
                    r, c, s = top
                    for d in drn:
                        if r + d[0] >= 0  and r + d[0] < row and c + d[1] >= 0 and c + d[1] < col:
                            if matrix[r + d[0]][c + d[1]] == None:
                                stack.append([r+d[0], c + d[1], sym])

    print("{} knights may be placed on a {} row {} column board.".format(count, row, col))