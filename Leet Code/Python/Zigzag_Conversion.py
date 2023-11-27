class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ""

        if numRows == 1:
            return s

        if numRows == 2:
            left = ""
            right = ""
            for i in range(len(s)):
                if i % 2 == 0:
                    left+=s[i]
                else:
                    right+=s[i]
            return left + right

        for i in range(numRows):
            if i == 0 or i == numRows-1:
                for j in range(i,len(s), 2*(numRows-1)):
                    ans+=s[j]
            else:
                for j in range(i,len(s), 2*(numRows-1)):
                    k = j + ((2*numRows - 4) - 2*(i-1))
                    ans+=s[j]
                    try:
                        ans+=s[k]
                    except:
                        pass
                
        return ans

print(Solution().convert("PAYPALISHIRING", 3))