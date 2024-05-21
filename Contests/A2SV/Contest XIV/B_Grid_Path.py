n = int(input())

for _ in range(n):
    n,m,k = [int(i) for i in input().split()]

    if k == (n*m)-1:
        print("YES")
    else:
        print("NO")