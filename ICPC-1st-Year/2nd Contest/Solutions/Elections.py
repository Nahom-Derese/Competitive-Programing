x = int(input())

y = [input().split() for i in range(x)]

for i in range(x):
    for j in range(3):
        y[i][j] = int(y[i][j])

for i in range(x):
    a,b,c = y[i]
    if y[i].count(max(y[i])) == 1:
        if y[i].index(max(y[i])) == 0:
            o = 0
            p = max(y[i]) + 1 - b
            q = max(y[i]) + 1 - c
        elif y[i].index(max(y[i])) == 1:
            o = max(y[i]) + 1 - a
            p = 0
            q = max(y[i]) + 1 - c
        elif y[i].index(max(y[i])) == 2:
            o = max(y[i]) + 1 - a
            p = max(y[i]) + 1 -b
            q = 0
    else:
            o = max(y[i]) + 1 - a
            p = max(y[i]) + 1 - b
            q = max(y[i]) + 1 - c


    print("{0} {1} {2}".format(o, p, q))
