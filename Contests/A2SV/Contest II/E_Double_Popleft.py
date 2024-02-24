from collections import deque

n, q = map(int, input().split())

nums = deque([int(i) for i in input().split()])
generated = []

def doublePopLeft(c):
    for j in range(c):
        if nums[0] > nums[1]:
            y = nums.popleft()
            x = nums.popleft()
            nums.append(x)
            nums.appendleft(y)
        else:
            x = nums.popleft()
            nums.append(x)
        


for i in range(q):
    query = int(input())
    max_index = nums.index(max(nums)) + 1
    doublePopLeft(min(query-1, max_index))
    if query > n:
        formula = (query - max_index) % n 
        print(nums[0], nums[formula])
    else:
        print(nums[0], nums[1])
    
    