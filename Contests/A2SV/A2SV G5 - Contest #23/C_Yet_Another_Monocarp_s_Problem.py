def helper(k, arr, h):
    poisns = 0
    for i in range(1, len(arr)):
        poisns += min(arr[i] - arr[i-1], k)
    return poisns >= h

def binary_search(arr, h):
    left, right = 1, 1 << 500
    while left < right:
        mid = left + (right - left) // 2
        
        if helper(mid, arr, h):
            right = mid
        else:
            left = mid + 1
    return left

def solve():
    n, h = [int(i) for i in input().split()]
    seconds = [int(i) for i in input().split()]
    seconds.append(float("inf"))
    return binary_search(seconds, h)
    
    

for _ in range(int(input())):
    print(solve())
