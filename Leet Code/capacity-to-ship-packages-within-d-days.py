class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def daysNeeded(limit):
            r = currentLoad = 0
            days = 1
            for r in range(len(weights)):
                currentLoad += weights[r]
                if currentLoad > limit:
                    days += 1
                    currentLoad = weights[r]

            return days

        l, r = [max(weights), sum(weights)]

        while l <= r:
            middle = l + (r - l) // 2
            if daysNeeded(middle) <= days:
                r = middle - 1
            else:
                l = middle + 1
        return l