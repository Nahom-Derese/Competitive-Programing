# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.tot = 0
        self.left_half = []
        self.right_half = []
        

    def addNum(self, num: int) -> None:
        if not self.tot:
            heappush(self.left_half, -num)
            self.tot += 1
            return
        
        self.tot += 1
        if self.tot % 2:
            if self.right_half and num > self.right_half[0]:
                x = heappushpop(self.right_half, num)
                heappush(self.left_half, -x)
            else:
                heappush(self.left_half, -num)
        else:
            if self.left_half and num < -self.left_half[0]:
                x = heappushpop(self.left_half, -num)
                heappush(self.right_half, -x)
            else:
                heappush(self.right_half, num)

        

    def findMedian(self) -> float:
        if self.tot % 2:
            return -1 * self.left_half[0]
        else:
            if self.left_half and self.right_half:
                return ((-self.left_half[0]) + self.right_half[0]) / 2
            return 0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()