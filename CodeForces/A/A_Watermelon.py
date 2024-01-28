n = int(input())
for i in range(1,n):
    if (n-i)% 2 == 0 and i%2 == 0:
        print('YES')
        break
else:
    print('NO')