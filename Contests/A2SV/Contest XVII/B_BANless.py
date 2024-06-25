def notA(x):
    return x in range(2, (3*n)+1, 3)

def solve():
    n = int(input())
    
    As = list(range(2, (3*n)+1, 3))
    BNs = list(range(1, (3*n)+1, 3)) + list(range(3, (3*n)+1, 3))
    BNs.sort(reverse=True)

    ans = []
    for a, b in zip(As, BNs):
        if a >= b:
            break
        ans.append((a, b))


    print(len(ans))
    for a, b in ans:
        print(a, b)

    
for _ in range(int(input())):
    solve()