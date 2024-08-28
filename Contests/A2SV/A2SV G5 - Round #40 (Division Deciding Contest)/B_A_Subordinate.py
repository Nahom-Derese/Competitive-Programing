nA, nB = [int(i) for i in input().split()]

k, m = [int(i) for i in input().split()]

nums_A = [int(i) for i in input().split()]
nums_B = [int(i) for i in input().split()]

if nums_A[k-1] < nums_B[-m]:
    print("YES")
else:
    print("NO")