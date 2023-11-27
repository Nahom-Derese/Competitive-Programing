for i in range(int(input())):
    n, k = list(map(int, input().split()))
    A = [k]
    A.extend(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    ans = 0

    for i in range(len(A)):
        if A[i] > B[i]:
            ans+=1
    
    print(ans)
