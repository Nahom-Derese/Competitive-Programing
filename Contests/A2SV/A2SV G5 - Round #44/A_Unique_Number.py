from collections import Counter

def solve():
    n = int(input())
    
    ai = [int(i) for i in input().split()]
    freq = Counter(ai)
    
    ans = -1
    _min = float("inf")
    
    for i, a in enumerate(ai):
        if freq[a] == 1:
            if _min > a:
                _min = a
                ans = i + 1
    print(ans)



for _ in range(int(input())):
    solve()
