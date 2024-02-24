
def tr_sq(grid):
    max_counts = []
    for i in grid:
        max_counts.append(i.count('1'))
    
    if len(set(max_counts)) < 3:
        return 'SQUARE'
    
    return 'TRIANGLE'

for i in range(int(input())):
    o = int(input())
    grid=[]
    for i in range(o):
        grid.append(input())
    print(tr_sq(grid))