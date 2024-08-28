from bisect import bisect_right

def prefix_sum(arr):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]
    return prefix



turns = list(range(1, 1000000, 4))
sums = prefix_sum(turns)

def countCards(index):
    bob = alice = 0
    for i in range(index):
        if i&1:
            bob+=turns[i]
        else:
            alice+=turns[i]

    return (alice, bob)

def solve():
    n = int(input())
    index = bisect_right(sums, n)-1
    alice, bob = countCards(index+1)
    if index & 1:
        alice += n - sums[index]
    else:
        bob += n - sums[index]

    print(alice, bob)

for _ in range(int(input())):
    solve()
