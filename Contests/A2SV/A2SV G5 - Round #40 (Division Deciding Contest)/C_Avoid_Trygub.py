def solve():
    n = int(input())
    
    a = list(input())
    
    a.sort(key=lambda x: ord(x))
    print("".join(a))

for _ in range(int(input())):
    solve()
