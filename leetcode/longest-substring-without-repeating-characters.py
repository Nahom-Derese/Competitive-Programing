class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = Counter()

        ans = r = l = 0

        while r < len(s):
            freq[s[r]]+=1

            while freq[s[r]]>1:
                freq[s[l]]-=1
                l+=1
            
            ans=max(ans,r-l+1)

            r+=1

        return ans