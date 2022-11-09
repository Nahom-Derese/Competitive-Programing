class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = dict()
        maxes = []
        maxe = 0
        for i in range(len(s)):
            if not a.get(s[i], False):
                a[s[i]] = True
                maxe += 1
            else:
                a = {}
                maxes.append(maxe)
                maxe = 0
        return max(maxes)

print(Solution.lengthOfLongestSubstring(Solution,'pwwkew'))
