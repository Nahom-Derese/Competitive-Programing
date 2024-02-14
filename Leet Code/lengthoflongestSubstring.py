class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        curr = set()
        right = 0
        ans = 1
        left = 0
        while right < len(s):
            while s[right] in curr:
                curr.remove(s[left])
                left += 1
            curr.add(s[right])
            ans = max(ans, len(curr))
            right += 1
        return ans