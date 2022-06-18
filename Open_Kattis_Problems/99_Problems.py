from cmath import log10
from math import trunc

a = int(input())



if trunc(log10(a).real) > 1.0:
    if a%100 == 49:
        a += 2
    c = round(a,-2) - 1

else:
     c = 99

print(c)