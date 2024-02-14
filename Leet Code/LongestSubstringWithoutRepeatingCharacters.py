class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = dict()
        maxes = []
        maxe = 0
        i = 0
        while i < len(s):
            if not a.get(s[i], False):
                a[s[i]] = [True,i]
                maxe += 1
            else:
                i = a.get(s[i])[1]
                a = {}
                maxe = 0
            maxes.append(maxe)
            i+=1
        ans = max(maxes) if len(maxes) > 0 else 0
        return ans

print(Solution.lengthOfLongestSubstring(Solution,"dvdf"))
