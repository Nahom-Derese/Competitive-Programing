from math import ceil

def solve():
    l,r,d = [int(i) for i in input().split()]
    l1, l2 = 1, r+1
    r1, r2 = l-1, 10**9 + 1

    if l1 <= d <= r1:
        return d
    if l2 <= d <= r2:
        return d

    return d * ceil(l2 / d)

for _ in range(int(input())):
    print(solve())
