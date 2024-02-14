from functools import cmp_to_key


n = int(input())

stu=[]

for i in range(n):
    S,X,M,P,C,B,E = input().split()
    X = int(X)
    M = int(M)
    P = int(P)
    C = int(C)
    B = int(B)
    E = int(E)

    M = M * 2
    P = P * 1.5
    National = X * (40/700)
    Entrance = (M+P+C+B+E )* 60/195
    
    stu.append((-1 * round(National+Entrance, 3) , S))

stu.sort()

for i in stu:
    val = i[0]
    print(i[1], "{:.3f}".format(-val))
