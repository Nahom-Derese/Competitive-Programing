from math import *

d,s  = input().split()
s_d= len(s)
i = 0
digit = 0
page_no = 0
while ((10**(s_d+i)) - int(s)) * s_d < int(d):
    if i == 0:
        digit += (10**(s_d) - int(s))*s_d
        page_no += (10**(s_d) - int(s))
    elif (((10**(s_d+i)) - (10**(s_d+i-1))) * (s_d+i) > int(d)):
        break;
    else:
        digit += ((10**(s_d+i)) - (10**(s_d+i-1))) * (s_d+i)
        page_no += ((10**(s_d+i)) - (10**(s_d+i-1)))
    i += 1

digit = int(d) - digit

if digit%(s_d+i) and digit > 0:
    print(-1)
else:
    page_no += (digit//(s_d+i))
    print(page_no)