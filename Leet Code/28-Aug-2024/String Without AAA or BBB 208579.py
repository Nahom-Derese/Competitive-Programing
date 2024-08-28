# Problem: String Without AAA or BBB - https://leetcode.com/problems/string-without-aaa-or-bbb

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []
        
        a_in_row = 0
        b_in_row = 0
        
        for _ in range(a + b):
            if (a > b and a_in_row < 2) or b_in_row == 2:
                res.append('a')
                a_in_row += 1
                b_in_row = 0
                a -= 1
            else:
                res.append('b')
                b_in_row += 1
                a_in_row = 0
                b -= 1
        return "".join(res)