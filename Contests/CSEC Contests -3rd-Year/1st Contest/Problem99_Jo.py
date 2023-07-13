def calc(n):

    i = 1
    k = 1
    while True:
        if n - i <= 0:
            return ''.join(map(str, range(1, k+1)))[n-1]
            break

        n -= i
        k += 1
        i += len(str(k))


for _ in range(int(input())):
    print(calc(int(input())))
