from math import factorial

n = int(input())
a = list(map(int,input().split()))


count = 0

perm = 0
for i in range(len(a)):
    x = a[i]
    if i != x:
        try:
            if a[x] == i or a[x] == (2*x-i):
                count+=1
        except:
            pass
    else:
        perm += 1

fact = 0
if perm > 1:
    fact = int(factorial(perm) / (factorial(perm-2)))

print(fact)

count += fact


print(count)