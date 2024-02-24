class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        r = 0
        while r < len(arr)-1 and arr[r] < arr[r+1]:
            r+=1
        l = len(arr)-1
        while l > 0 and arr[l-1] > arr[l]:
            l-=1
        return r == l and l!= len(arr)-1 and r!=0