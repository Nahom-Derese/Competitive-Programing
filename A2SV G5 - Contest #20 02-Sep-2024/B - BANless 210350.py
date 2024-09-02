# Problem: B - BANless - https://codeforces.com/gym/528792/problem/B

def solve():
    n = int(input())
    
    if n == 1:
        print(1)
        print(2,3)
        return
    
    Bs = list(range(1, (3*n)+1, 3))
    Ns = list(range(3, (3*n)+1, 3))
    
    Ns.sort(reverse=True)
    
    ans = []
    for a, b in zip(Bs, Ns):
        if a > b:
            break
        ans.append((a, b))
    print(len(ans))
    for a, b in ans:
        print(a, b)

for _ in range(int(input())):
    solve()