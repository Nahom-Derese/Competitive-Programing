from collections import Counter

t = int(input())


for i in range(t):
    n = int(input())
    s = input()

    s = "".join(s.split())

    x = dict(Counter(s))

    total_Unique = len(x)
    count = 0

    for i in x:
        if x[i]%2==0:
            count+=1
    
    if count == total_Unique or count == total_Unique-1:
        print("YES")
    else:
        print("NO")