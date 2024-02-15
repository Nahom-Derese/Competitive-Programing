class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        freq_so_far = defaultdict(int)
        ans = 0
        while r < len(s):
            freq_so_far[s[r]]+=1

            while k < (r-l+1 - max(freq_so_far.values())):
                freq_so_far[s[l]]-=1
                l+=1

            ans = max(ans, r-l+1)
            r+=1
        return ans
