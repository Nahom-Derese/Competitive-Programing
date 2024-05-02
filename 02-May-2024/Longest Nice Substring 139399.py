# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        
        if n < 2:
            return ""
        
        ss = set(s)
        for ii in range(n):
            if s[ii].swapcase() not in ss:
                s1 = self.longestNiceSubstring(s[0:ii])
                s2 = self.longestNiceSubstring(s[ii+1:])
                return max(s1, s2, key=len)
        return s