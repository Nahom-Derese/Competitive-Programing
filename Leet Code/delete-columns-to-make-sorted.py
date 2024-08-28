class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        c = 0
        for j in range(n):
            for i in range(1, len(strs)):
                if strs[i-1][j] > strs[i][j]:
                    c+=1
                    break
        return c