T = int(input())

ans = []

for j in range(T):
    n, m = [int(i) for i in input().split()]
    dict = {}
    for i in range(n):
        k = [int(i) for i in input().split()]
        dict[k[len(k)-1]] = k[1:len(k)-1]

    o = [int(i) for i in input().split()]

    answer = 0

    for i in dict:
        u = [o[p-1] for p in dict[i]]
        answer += int(min(u) * i)
        for p in dict[i]:
            o[p-1] -= 1

    ans.append(int(answer))

for i in ans:
    print(i)