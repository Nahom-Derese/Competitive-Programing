# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth = nlargest(k, nums)
        self.k = k
        heapify(self.kth)
        
    def add(self, val: int) -> int:
        if len(self.kth) < self.k:
            heappush(self.kth, val)
        elif val > self.kth[0]:
            heappushpop(self.kth, val)
            
        return self.kth[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)