for i in range(int(input())):
    n, m = map(int, input().split())
 
    P = [int(i) for i in input().split()]
    V = [int(i) for i in input().split()]
 
    p_s = sorted(P)
    v_s = sorted(V)
    v_s.reverse()
    ans = 0
    l , r , q = [0,-1,0]
    
    while q < n:
        l_d = abs(p_s[l] - v_s[l])
        r_d = abs(p_s[r] - v_s[r])
        
        if l_d > r_d:
            ans+=l_d
            l+=1 
        else:
            ans+= r_d
            r-=1
        q+=1 
    
    
    print(ans)