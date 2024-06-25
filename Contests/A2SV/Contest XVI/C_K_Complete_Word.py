t = int(input())

for i in range(t):
    n, k = [int(i) for i in input().split()]
    s = input()

    counts = [set() for i in range(k)]
    dif_pals = []
    ans = 0
    
    for i in range(0,n,k):
        dif_pal = 0

        l = i
        r = i + k - 1
        
        while r > l:
            dif_pal += s[r] != s[l]
            r-=1
            l+=1

        dif_pals.append(dif_pal)


    for i in range(0,n,k):
        for j in range(i, i+k):
            # print(s[j], end=" ")
            if s[j] not in counts[j%k]:
                ans+=1
                counts[j%k].add(s[j])


    print(ans + min(dif_pals) - k)
    # print(dif_pals)