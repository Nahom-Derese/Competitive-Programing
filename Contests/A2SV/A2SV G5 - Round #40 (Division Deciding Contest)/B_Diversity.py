s = list(input())
k = int(input())

uniques = len(set(s))

if len(s) < k:
    print("impossible")
else:
    if uniques >= k:
        print(0)
    else:
        print(k - uniques)