class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for i in range(len(arr)):
            u = arr.index(max(arr[:len(arr)-i]))
            ans.append(u+1)
            arr[:u+1] = arr[:u+1][::-1]
            ans.append(len(arr)-i)
            arr[:len(arr)-i] = arr[:len(arr)-i][::-1]
        return ans