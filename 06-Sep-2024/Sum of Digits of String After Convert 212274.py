# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        s = "".join(list(map(lambda char: str(ord(char) - ord("a") + 1), list(s))))

        while k:
            s = str(sum(list(map(int, list(s)))))
            k-=1

        return int(s)