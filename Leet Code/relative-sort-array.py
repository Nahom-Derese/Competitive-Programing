class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        x = Counter(arr1)
        ans = []
        for i in arr2:
            ans.extend([i] * x[i])
        
        ans.extend(sorted([i for i in arr1 if i not in arr2]))
        return ans