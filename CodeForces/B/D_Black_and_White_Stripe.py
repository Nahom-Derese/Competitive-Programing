for i in range(int(input())):
    n, m = map(int, input().split())

    BW = input()

    ans = 0
    wind = BW[:m-1].count("B")
    l, r = [0, m-1]

    while(r < n):
        if BW[r] == "B":
            wind+=1

        ans = max(ans, wind)

        if BW[l] == "B":
            wind-=1

        r+=1
        l+=1

print(m-ans)
        