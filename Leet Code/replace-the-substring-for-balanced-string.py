class Solution:
    def balancedString(self, s: str) -> int:
        x = Counter(s)
        l = len(s)//4

        for k in list(x.keys()):
            x[k]-=l
            if x[k]<=0:
                x.pop(k)
        
        if x == Counter():
            return 0

        ans = float("inf")
        l = r = 0
        freq = Counter()
        while r < len(s):
            freq[s[r]]+=1
            
            while len(x-freq) == 0 and l<=r:
                ans = min(ans, r-l+1)
                freq[s[l]]-=1
                l+=1

            r+=1
            
        return ans