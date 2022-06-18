from cmath import log10
from math import trunc

a = int(input())

if log10(a).real > 1.0:
    if a % 100 >= 49:
        a = a // 100
        ans = str(a) + "99"
        a = int(ans)
    else:
        digit = trunc(log10(a).real)
        b = a%100
        a -= b+1
else:
    a = 99

print(a)