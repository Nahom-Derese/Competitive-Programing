class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def rec(idx):

            if idx == 1:
                return [1,1]

            l = 0
            r = 1
            o = rec(idx-1)
            
            ans = [1]
            while r < len(o):
                ans.append(o[l]+o[r])
                r+=1
                l+=1
            ans.append(1)
            
            return ans

        if not rowIndex:
            return [1]
        return rec(rowIndex)