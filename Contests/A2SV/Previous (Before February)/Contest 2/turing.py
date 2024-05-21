"""
First, inorder to solve the problem, it's better to sort the numbers in increasing orders then by decreasing or 
increasing the numbers in the list, we can find the minimum number of operations to make the list a exactly have 
numbers from 1 to N.

The idea is to find the minimum number of operations to make the list a have numbers from 1 to N.
"""

""" Approach:
1. Sort the list in increasing order.
2. Try to make the numbers in the list equal to their index + 1, if the number is greater than the index + 1, 
   then we can make the number equal to the index + 1 by decreasing the number by 1. If the number is less than the
   index + 1, then we can make the number equal to the index + 1 by increasing the number by 1. when increasing or 
   decreasing the number, we need to keep track of the number of operations needed to make the number equal to the
3. If the number is equal to the index + 1, then we don't need to do anything. so we can skip the number, without 
    increasing the number of operations.
4. After we make the number equal to the index + 1, we can increment the index by 1.
5. Repeat the process until we reach the end of the list.
6. The minimum number of operations is the sum of the number of operations needed to make the number equal to the 
    index + 1.
"""

def solution(nums):
    nums.sort()
    n = len(nums)
    ans = 0
    for i in range(n):
        ans += abs(nums[i] - (i + 1))
    return ans

# Time complexity: O(nlogn)

# Test cases
print(solution([1, 2, 3])) # 0
print(solution([3, 2, 1])) # 3
print(solution([1, 3, 2])) # 1
print(solution([1, 2, 3, 4])) # 0
print(solution([4, 3, 2, 1])) # 6
print(solution([1, 4, 2, 3])) # 2
print(solution([1, 2, 4, 3])) # 1
print(solution([1, 2, 3, 4, 5])) # 0
print(solution([5, 4, 3, 2, 1])) # 10
print(solution([1, 5, 2, 4, 3])) # 3
print(solution([1, 2, 4, 5, 3])) # 2