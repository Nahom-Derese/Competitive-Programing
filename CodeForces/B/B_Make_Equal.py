def x():
    for i in range(1,o):
        if n[i-1] < val:
            return "NO"
        e = n[i-1]-val
        n[i-1] -= e
        n[i] += e
    return "YES"


    
for i in range(int(input())):
    o = int(input())
    n = list(map(int, input().split()))
    
    val = sum(n) // o
    print (x())
