t = int(input())

ans = []

for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    x,y = [False,False]
    
    check = 0
    c=0
    for j in range(0,n,2):
        if a[j]%2 == 0:
            check+=1
        c+=1
    
    x = check == c or check == 0

    check = 0
    c=0
    for j in range(1,n,2):
        if a[j]%2 == 0:
            check+=1
        c+=1
    
    y = check == c or check == 0
    
    ans.append("YES" if x and y else "NO")


for i in ans:
    print(i)