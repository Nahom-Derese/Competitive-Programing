n, q = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()
pre_sum = [0] * (n+1)

for i in range(1, n+1):
    pre_sum[i] = pre_sum[i-1] + arr[i-1]

for i in range(q):
    x, y = map(int, input().split())
    bought = pre_sum[-1] - pre_sum[-x-1]
    free = pre_sum[-x+y-1] - pre_sum[-x-1]
    print(free)
