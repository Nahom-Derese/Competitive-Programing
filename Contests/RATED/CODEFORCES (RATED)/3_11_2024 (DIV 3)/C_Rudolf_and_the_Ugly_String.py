for i in range(int(input())):
    n = int(input())
    a = input()
    
    l = ans = 0
    r = 2

    while r < n:
        if a[l] == 'm' and a[l+1] == 'a' and a[r] == 'p':
            ans+=1
            l+=3
            r+=3
        elif a[l] == 'p' and a[l+1] == 'i' and a[r] == 'e':
            ans+=1
            l+=3
            r+=3
        else:
            l+=1
            r+=1
    
    print(ans)