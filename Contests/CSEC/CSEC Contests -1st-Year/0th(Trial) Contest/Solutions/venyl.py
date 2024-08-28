from math import *
inp = int(input())

a = input().split()

for i in range(len(a)):
    a[i] = pi * (int(a[i]))**2

a.sort()
ans = 0

for i in range(len(a)):
    if len(a)>=2:
        ans += a[len(a)-1] - a[len(a)-2]
        a.pop(len(a)-1)
        a.pop(len(a)-1)
    elif len(a)!=0:
        ans += a[0]
        break
    else:
        break

print('%.6f'%ans)