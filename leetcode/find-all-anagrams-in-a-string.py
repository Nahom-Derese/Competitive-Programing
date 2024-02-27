class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        targetFreq = Counter(p)

        r = len(p)-1
        l = 0
        ans = []
        currentFreq = Counter(s[:r])
        while r < len(s) :
            currentFreq[s[r]]+=1
            
            if currentFreq == targetFreq:
                ans.append(l)

            currentFreq[s[l]]-=1

            if currentFreq[s[l]] == 0:
                del(currentFreq[s[l]])
            
            r+=1
            l+=1
        
        return ans