class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = ""
        
        for i in s:
            if i.isalnum():
                check+=i.lower()
        
        r = len(check)-1
        l = 0

        print(check)
        while l < r:
            if check[l] != check[r]:
                return False
            l+=1
            r-=1

        return True