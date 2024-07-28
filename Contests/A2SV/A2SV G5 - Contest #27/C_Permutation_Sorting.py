def solve():
    n = int(input())
    nums = [int(i) for i in input().split()]
    
    indices = {num: i for i, num in enumerate(nums)}
    
    ans = 0
    for i in range(1, n):
        ans+=indices[i] > indices[i+1]

    print(ans)

for _ in range(int(input())):
    solve()
