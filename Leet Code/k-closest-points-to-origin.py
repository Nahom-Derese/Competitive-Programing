class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(a):
            x, y = a
            return sqrt(x**2 + y**2)
        
        return sorted(points, key=lambda i: distance(i))[:k]