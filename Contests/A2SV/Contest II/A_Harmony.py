from sys import stdin

input = stdin.readline

for i in range(int(input())):
    if i:
        input()
        
    n, x = list(map(int, input().split()))
    

    a = sorted([int(i) for i in  input().split()])
    b = sorted([int(i) for i in  input().split()], reverse=True)
    

    for i in range(len(a)):
        if a[i] + b[i] > x:
            print("No")
            break
    else:
        print("Yes")

