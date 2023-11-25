for i in range(int(input())):
    n, k = map(int, input().split())
    
    integers = list(map(int, input().split()))

    preference = list(map(int, input().split()))

    integers.sort()
    preference.sort(reverse=True)
    
    c = preference.count(1)

    ans = sum(integers[-k:])

    i=0
    j=0

    while i < len(integers[:-k]) and j < len(preference)-c:
        ans += integers[i]
        i+=preference[j]-1
        j+=1
    
    if c > 0:
        for i in integers[-c:]:
            ans += i
        
    print(ans)
