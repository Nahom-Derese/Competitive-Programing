# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        count = Counter()
        itr = 0
        ans = 0
        
        while itr < len(s):
            if count[s[itr]]:
                ans+=1
                count = Counter()
            count[s[itr]]+=1
            itr+=1


        return ans+1