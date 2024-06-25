n = int(input())

s = input()
r = 0

def prefix_sum(arr):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]
    return prefix


pre_sum = prefix_sum([i for i in range(60)])

while r < n:
    index = pre_sum[r]
    if index >= n:
        break
    print(s[index], end="")
    r += 1