from collections import Counter

t = int(input())

for i in range(t):
    n = int(input())
    a = input()

    l = a.split('W')

    if n == 1:
        print('NO')
        continue
    if len(l)==1:
        print('YES')
        continue

    for i in l:
        x = Counter(i)
        
        if 'R' in x and 'B' in x:
            print('NO')
            break

    