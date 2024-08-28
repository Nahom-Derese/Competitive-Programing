# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        n=len(s)
        dp=[-1]*(n+1)
        dp[n]=0
        for i in range(n-1,-1,-1):
            temp=''
            mini=maxsize
            for j in range(i,n):
                temp+=s[j]
                if temp==temp[-1::-1]:
                    cuts=1+dp[j+1]
                    mini=min(mini,cuts)
            dp[i]=mini
        return dp[0]-1