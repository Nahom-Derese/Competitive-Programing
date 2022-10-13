class Solution:
    def isPalindrome(self, s: str) -> bool:
        pure = ''
        for i in s:
            if(i.isalnum()):
                pure+=i.lower()
        if(pure == pure[::-1]):
            return True
        return False