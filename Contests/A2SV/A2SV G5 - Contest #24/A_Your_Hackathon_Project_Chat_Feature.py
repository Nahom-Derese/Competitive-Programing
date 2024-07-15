def solve():
    n = int(input())
    s = input()

    count = 0
    for i in range(n-1, -1,-1):
        if s[i] != ")":
            break
        count+=1
    
    rest = n - count
    
    return rest < count

for _ in range(int(input())):
    if solve():
        print("Yes")
    else:
        print("No")