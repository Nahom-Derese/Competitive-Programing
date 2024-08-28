from heapq import *

def solve():
    input()

    nums = [-int(i) for i in input().split()]
    alice = bob = 0

    heapify(nums)

    for i in range(len(nums)):
        if i&1:
            num = abs(heappop(nums))
            if num&1:
                bob+=num
        else:
            num = abs(heappop(nums))
            if not num&1:
                alice+=num

    if alice == bob:
        print("Tie")
    if alice > bob:
        print("Alice")
    if alice < bob:
        print("Bob")

for _ in range(int(input())):
    solve()
