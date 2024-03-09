class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        p = [0 for x in range(n+1)]

        for i in range(n):
            if s[i] == '1':
                p[i+1] = p[i] + 1
            else:
                p[i+1] = p[i]

        prefix_sum = p[1:]
        ans = 0
        for i in range(1, len(s)):
            z = i - prefix_sum[i - 1]
            o = prefix_sum[-1] - prefix_sum[i - 1]
            ans = max(ans, z + o)
        return ans