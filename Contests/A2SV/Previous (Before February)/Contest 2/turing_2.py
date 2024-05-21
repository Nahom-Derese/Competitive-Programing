

# Given a list of integers X, a list of integers S, and a list of integers Y, 
# where X[i] is the position of the ith fly, S[i] is the maximum distance the ith frog can jump, 
# and Y[i] is the position of the ith frog, return a list of integers where the ith integer is the number 
# of flies the ith frog can catch.

"""
 Approach:
 1. Create a list p_s of size max(Y) and initialize all the elements to 0.
 
 2. For each fly in Y, set p_s[fly - 1] to 1.
 
 3. Compute the prefix sum of p_s.
 
 4. For each frog, find the range of flies it can catch.
 
 5. The number of flies the frog can catch is the difference between the prefix sum of the right index and the prefix sum of the left index.
 
 6. Return the list of the number of flies each frog can catch.
"""

"""
  Detailed Approach about the solution:

  1. Create a list p_s of size max(Y) and initialize all the elements to 0.

  2. For each fly in Y, set p_s[fly - 1] to 1. meaning that there is a fly at position fly.

  3. Compute the prefix sum of p_s.

  4. For each frog, find the range of flies it can catch. The range of flies the frog can catch is from X[i] - S[i] to X[i] + S[i], since their toungue's size is S[i].

  5. The number of flies the frog can catch is the difference between the prefix sum of the right index and the prefix sum of the left index. The prefix sum of the right index is p_s[X[i] + S[i]] and the prefix sum of the left index is p_s[X[i] - S[i] - 1].

"""


"""
Time complexity: O(n + m), where n is the length of X, S, and Y, and m is the maximum value in Y.
Space complexity: O(m)
"""


def prefix_sum(arr):
	n = len(arr)
	prefix = [0] * n
	prefix[0] = arr[0]
	for i in range(1, n):
		prefix[i] = prefix[i - 1] + arr[i]
	return [0] + prefix

def solve(X, S, Y):
	p_s = [0] * max(Y)
	
	for fly in Y:
		p_s[fly - 1] = 1

	p_s = prefix_sum(p_s)
	ans = []
	for i in range(len(X)):
		left, right = [max(0, X[i] - S[i] - 1), min(len(p_s)-1, X[i] + S[i])]
		ans.append(p_s[right] - p_s[left ])
	
	return ans

# # Test cases
print(solve([1, 4, 5], [2, 3, 5], [2, 3, 5])) # [2, 3, 3]