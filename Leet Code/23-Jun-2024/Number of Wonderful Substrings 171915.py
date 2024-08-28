# Problem: Number of Wonderful Substrings - https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        masks = [0] * (1 << 10)
        masks[0] = 1
        cur = 0
        ans = 0
        for x in word:
            cur ^= 1 << (ord(x) - ord('a'))
            ans += masks[cur]
            for i in range(10):
                ans += masks[(1 << i) ^ cur]
            masks[cur] += 1
        return ans