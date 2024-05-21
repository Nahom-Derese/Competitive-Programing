_ = int(input())
nums = list(map(int, input().split()))

x = sum(nums)
if x % 2 == 0:
    print(x)
else:
    ans = 0
    odds = []
    for i in nums:
        if i % 2:
            odds.append(i)
        ans += i
    print(ans-min(odds))
    