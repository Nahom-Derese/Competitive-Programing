import math

k,d,t = map(int,input().split())

if k<=d:
    period = d
else:
    period = math.ceil(k/d)*d


cooking = k+period

num = (2*t)//cooking

carry = 2*t-(num*cooking)

if carry>(2*k):
    print(num*period+carry-k)
else:
    print(num*period+(carry/2))