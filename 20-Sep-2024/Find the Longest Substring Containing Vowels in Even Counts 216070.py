# Problem: Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        dic = {0:-1}
        ans = x_or = 0

        for i, char in enumerate(s):
            
            if char in ['a', 'e', 'i', 'o', 'u']:
                x_or ^= (ord(char) & 31)
            
            if x_or in dic:
                ans = max(ans, i - dic[x_or])
            else:
                dic[x_or] = i

        return ans