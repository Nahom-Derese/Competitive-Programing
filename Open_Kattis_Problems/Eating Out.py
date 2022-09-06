k , a,b,c = [int(i) for i in input().split()]

if k*2+1 > a+b+c:
    print("possible")
else:
    print("impossible")