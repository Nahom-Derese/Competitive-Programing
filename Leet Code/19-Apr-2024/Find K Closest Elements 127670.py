# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for i in range(len(arr)):
            heappush(heap, (abs(x - arr[i]), arr[i]))

        ans = []
        for i in range(k):
            ans.append(heappop(heap)[1])

        return sorted(ans)