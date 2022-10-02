from math import *

n = input()

sum = 0
for i in n:
    sum += ord(i)

total = (int(sum / 100) + 1) * 100

per = sum / total
selflove = floor(per*100)

ans = 100 - selflove

print(str(ans) + '%')