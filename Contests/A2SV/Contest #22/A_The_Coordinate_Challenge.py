def solve():
    n = abs(int(input()))
    
    q1, r1= divmod(n, 3) 
    
    if n == 1:
        print(2)
        return
    print(q1 + int(bool(r1)))

for _ in range(int(input())):
    solve()
