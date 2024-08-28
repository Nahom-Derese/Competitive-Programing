class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        maps = {}
        for i in range(len(s)):
            maps[s[i]] = i
        
        ans = []
        i = 0
        while i < len(s):
            y = maps[s[i]]
            while i < y:
                y = max(y, maps[s[i]])
                i+=1
            ans.append(i+1 - sum(ans))
            i+=1

        return ans