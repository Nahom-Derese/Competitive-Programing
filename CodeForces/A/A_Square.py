a = int(input())

ans = []
for i in range(a):
    xCoordinate = []
    yCoordinate = []
    for j in range(4):
        x, y = map(int, input().split())
        xCoordinate.append(x)
        yCoordinate.append(y)
    ans.append((max(xCoordinate) - min(xCoordinate) )* (max(yCoordinate) - min(yCoordinate)))

for i in ans:
    print(i)