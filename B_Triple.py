from collections import Counter

t = int(input())


for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    x = Counter(a)

    for i in x:
        if x[i] > 2:
            print(i)
            break
    else:
        print(-1)
