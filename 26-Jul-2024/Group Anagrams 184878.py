# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp ={}
        
        for s in strs:
            f=str(sorted(s))
            if f not in mp:
                mp[f]=[]
            mp[f].append(s)
        return list(mp.values())


