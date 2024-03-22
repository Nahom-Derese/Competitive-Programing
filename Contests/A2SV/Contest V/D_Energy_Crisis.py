from collections import defaultdict

n, k = [int(i) for i in input().split()]

a = sorted([int(i) for i in input().split()], reverse=True)


def checker(m):
    global a
    available = 0
    for i in range(n):
        if a[i] - m >= 0:
            available += a[i] - m
        else:
            available -= ((m - a[i]) / (1-k/100))
    return available >= 0

l = 0
r = a[0]
for i in range(90):
    m = (r + l) / 2

    if checker(m):
        l = m
    else:
        r = m

print(f"{l:.9f}")
