t = int(input())


for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    l = 0
    r = n-1

    bob = 0
    alice = 0

    possible_ans= []

    while l<r:
        if alice == bob:
            possible_ans.append(l + (n-r) - 1)
        if alice + a[l] < bob + a[r]:
            alice += a[l]
            bob += a[r]
            l += 1
        else:
            alice += a[l]
            bob += a[r]
            r -= 1
    print(max(possible_ans))