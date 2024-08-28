def solve():
    n,m,k = [int(i) for i in input().split()]
    
    a  = list(input())
    b  = list(input())
    
    a.sort()
    b.sort()

    aa = bb = a_p = b_p = 0
    c = ""
    
    while a_p < len(a) and b_p < len(b):

        if a[a_p] > b[b_p]:
            if bb == k:
                c+=a[a_p]
                bb=0
                a_p+=1
                continue
            
            c+=b[b_p]
            bb+=1
            aa=0
            b_p+=1
        
        else:
            if aa == k:
                c+=b[b_p]
                aa=0
                b_p+=1
                continue
            c+=a[a_p]
            aa+=1
            bb=0
            a_p+=1

    print(c)

        

for _ in range(int(input())):
    solve()
