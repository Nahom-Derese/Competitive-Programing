import sys
from bisect import *


arr = []

def merge(arr1, arr2):
    i = j = 0
    _sorted = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i][0] < arr2[j][0]:
            _sorted.append(arr1[i])
            i += 1
        else:
            _sorted.append(arr2[j])
            j += 1
    _sorted += arr1[i:]
    _sorted += arr2[j:]
    return _sorted

def check(arr1, arr2):
    i = j = 0
    copy_arr1 = list(map(lambda x: x[0], arr1))
    copy_arr2 = list(map(lambda x: x[0], arr2))
    for i in range(len(arr1)):
        arr1[i][0] += bisect_left(copy_arr2, arr1[i][0])
        arr2[i][0] += bisect_left(copy_arr1, arr2[i][0])
        


def merge_sort(left, right):
    global arr
    if not (right - left):
        return [arr[right]]
    mid = left + (right - left) // 2
    left_arr = merge_sort(left, mid)
    right_arr = merge_sort(mid + 1, right)
    
    
    check(left_arr, right_arr, left, mid)
    

    return merge(left_arr, right_arr)


for i in range(int(input())):
    
    n = int(sys.stdin.readline().strip())

    arr = sys.stdin.readline().strip().split()
    for i in range(len(arr)):
        arr[i] = [int(arr[i]), i]
    
    ans = [0]*(2**n)
    for num, i in merge_sort(0, len(arr)-1):
        ans[i] = num
    print(*ans)
        
    
