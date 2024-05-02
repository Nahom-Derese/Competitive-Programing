# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        itr = -1
        if len(a) > len(b):
            b = "0"*(len(a)-len(b)) + b
        if len(a) < len(b):
            a = "0"*(len(b)-len(a)) + a
        

        ans = ""
        while itr >= -len(b):
            x = int(a[itr])
            y = int(b[itr])

            q = x ^ y ^ carry
            carry = x & y | x & carry | y & carry

            ans+=str(q)
            itr-=1
    
        if carry:
            ans+="1"
        return ans[::-1]