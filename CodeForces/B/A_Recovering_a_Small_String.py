for i in range(int(input())):
    n = int(input())
    
    alpha = "-abcdefghijklmnopqrstuvwxyz"

    ans = []

    for i in range(len(alpha)-1,0,-1):
        if n - i > 1:
            n -= i
            ans.append(alpha[i])
            break
    
    for i in range(len(alpha)-1,0,-1):
        if n - i > 0:
            n -= i
            ans.append(alpha[i])
            break
            
    ans.append(alpha[n])
    
    print("".join(ans[::-1]))
    