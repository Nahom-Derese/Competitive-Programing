from itertools import product 

b = int(input())

for i in product('12', repeat= b):
    print(' '.join(i))
