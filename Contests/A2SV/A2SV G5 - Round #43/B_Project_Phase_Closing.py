from math import ceil

n, m, k = [int(i) for i in input().split()]

x = ceil(k/2)

r = ceil(x / m)
d = x - ((r - 1) * m)

s = "R"
if k & 1:
    s = "L"

print(r, d, s)