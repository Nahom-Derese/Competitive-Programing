# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        map_ = {}
        reverse_map = {}
        for i in range(len(s)):
            char1, char2 = s[i], t[i]

            if char1 in map_ and map_[char1] != char2:
                return False
            if char2 in reverse_map and reverse_map[char2] != char1:
                return False
            
            map_[char1] = char2
            reverse_map[char2] = char1


        return True