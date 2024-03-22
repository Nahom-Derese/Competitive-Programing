t = int(input())
nums = sorted([int(i) for i in input().split()])
a = int(input())

def search(target):
    res = left = 0
    right = t - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid+1
    return right+1

for i in range(a):
  target = int(input())

  print(search(target))
