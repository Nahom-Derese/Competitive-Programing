from math import ceil
def solve():
    n, k = [int(i) for i in input().split()]
    
    if n > k:
        k*=ceil(n / k)

    q, r = divmod(k, n)
    if r:
        q += 1
    
    return q


for _ in range(int(input())):
    print(solve())
