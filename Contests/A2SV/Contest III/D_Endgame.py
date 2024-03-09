from bisect import *

n, k, A, B = [int(i) for i in input().split()]
avengers = sorted([int(i) for i in input().split()])

def rec(start, end):

    l = bisect_left(avengers, start)
    r = bisect_right(avengers, end)

    curr = 0


    if r - l :
        curr =  B * (end - start + 1)  * (r - l)
    else:
        curr =  A

    
    if start == end:
        return curr
    
    if not r - l:
        return A

    middle = start + (end - start) // 2 

    right = rec(start, middle)
    left = rec(middle+1, end)
    
    return min(curr, left + right)

print(rec(1, 2**n))
