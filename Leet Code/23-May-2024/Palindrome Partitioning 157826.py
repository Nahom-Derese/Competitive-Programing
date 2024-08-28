# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        result = []
        
        for i in range(n):
            dp[i][i] = 1
        
        for k in range(2, n + 1):
            for i in range(n - k + 1):
                j = i + k - 1
                if s[i] == s[j]:
                    if k == 2 or dp[i + 1][j - 1]:
                        dp[i][j] = 1

        def dfs(start, path):
            if start == n:
                result.append(path[:])
                return
            for end in range(start, n):
                if dp[start][end]:
                    dfs(end + 1, path + [s[start:end+1]])

        dfs(0, [])
        return result