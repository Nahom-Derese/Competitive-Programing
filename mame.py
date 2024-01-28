from math import log2, ceil

for i in range(int(input())):

    a = int(input())

    if 2**19%a == 0 and a > 1:
        print(1)
    else:
        print(ceil(log2(a)))