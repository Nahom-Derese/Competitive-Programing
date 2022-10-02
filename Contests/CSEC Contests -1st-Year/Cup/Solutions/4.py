from math import *

n = input().split('+')

ans = ""

for i in n:
    
    for j in i:
        if j.isalpha():
            ans += i[1:i.find(j)] + " + "
            break

    if ans == '' and i == n[len(n)-1]:
        ans += "0"
if ans[-2] == '+':
    ans = ans[0:-3]

print(ans)