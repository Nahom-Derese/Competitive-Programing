def solve():
    order = input()

    mapp = { j:i for i, j in enumerate(list(order)) }

    word = list(input())

    ans = 0
    for i in range(1, len(word)):
        ans += abs(mapp[word[i]] - mapp[word[i-1]])
    
    print(ans)


for _ in range(int(input())):
    solve()
