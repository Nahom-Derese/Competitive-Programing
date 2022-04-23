while True:
    try:
        X = input().split()
        a = int(X[0])
        b = int(X[1])
        ans = a *(2*b)
        print(ans)
    except:
        break