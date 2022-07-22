from math import factorial

a = int(input())

ans = 1
fact = 1

for i in range(1,a+1):
    fact *= i
    ans += 1 / fact

print(round(ans,15))