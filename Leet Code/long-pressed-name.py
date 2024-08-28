class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l = r = 0

        while r < len(typed) and l < len(name):
            temp = typed[r]
            print(temp)
            if typed[r] == name[l]:
                c_1 = 0
                c_2 = 0
                while  r < len(typed) and typed[r] == temp:
                    r+=1
                    c_1+=1
                while l < len(name) and name[l] == temp:
                    l+=1
                    c_2+=1
                if c_2 > c_1:
                    return False
            else:
                return False
        return r == len(typed) and l == len(name)