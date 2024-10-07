# Problem: C - Coffee Dilemma - https://codeforces.com/gym/528792/problem/C

from heapq import heappushpop, heappush
n = int(input())

nums = [int(i) for i in input().split()]

running_sum = 0
count = 0
negatives = []

for num in nums:
    if running_sum + num >= 0:
        if num < 0:
            heappush(negatives, num)
        running_sum += num
        count += 1
    else:
        if negatives and negatives[0] < num:
            running_sum -= heappushpop(negatives, num)
            running_sum += num

print(count)