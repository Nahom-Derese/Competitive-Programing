import math

n = int(input())

def helper(x):
    eat_count = 0
    n_copy = n
    while n_copy > 0:
        eat_count += x
        n_copy_copy = n_copy
     
        n_copy -= x
        n_copy -= math.floor(n_copy * 0.1)
            
    return eat_count > n//2

def binary_search(num):
    left, right = 0, num
    while left < right:
        mid = left + (right - left) // 2
        if helper(mid):
            right = mid 
        else:
            left = mid + 1
    return left

print(binary_search(n//2 + 1))