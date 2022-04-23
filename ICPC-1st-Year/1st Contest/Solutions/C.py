x = int(input())

y = [input().split() for i in range(2)]

price = 0
for i in range(x):
    y[0][i] = int(y[0][i])
    y[1][i] = int(y[1][i])
    price += y[0][i] * y[1][i]

ans = "{0} {1}".format(sum(y[0]), price)

print(ans)