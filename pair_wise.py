x = int(input())
y = [int(i) for i in input().split()]
maxx = float('int')
maxx *=-1
for i in range(1, x):
    r = i
    l = i - 1

    maxx = max(maxx, y[l] * y[r])

print(maxx)
