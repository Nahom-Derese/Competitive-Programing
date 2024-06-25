t = int(input())


for i in range(t):
    n = int(input())
    nums = [int(i) for i in input().split()]
    
    and_ = (1 << 32) -1

    for i in nums:
        and_ &= i

    print(and_)