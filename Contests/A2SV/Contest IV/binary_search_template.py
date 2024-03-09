

while left < right:
    mid = left + (right - left) // 2
    if is_possible(mid): # try to minimize solution
        right = mid
    else:
        left = mid + 1

    return left