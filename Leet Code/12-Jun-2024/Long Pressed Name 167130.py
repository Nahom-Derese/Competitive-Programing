# Problem: Long Pressed Name - https://leetcode.com/problems/long-pressed-name/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        itr1 = itr2 = 0
        
        while itr1 < len(name) and itr2 < len(typed):
            
            if name[itr1] != typed[itr2]:
                return False
            
            x = name[itr1]
            count1 = count2 = 0
            while itr1 < len(name) and x == name[itr1]:
                itr1+=1
                count1+=1
            while itr2 < len(typed) and  x == typed[itr2]:
                itr2+=1
                count2+=1
            
            if count1 > count2:
                return False
        
        return itr2 == len(typed) and itr1 == len(name)