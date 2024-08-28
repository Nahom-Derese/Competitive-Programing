# Problem: Compare Version Numbers - https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")

        v1 = v2 = 0
        for i in range(len(version1)):
            v1+=int(version1[i]) / 10**i
        for i in range(len(version2)):
            v2+=int(version2[i]) / 10**i
        
        if v1 > v2:
            return 1
        if v1 < v2:
            return -1
        return 0