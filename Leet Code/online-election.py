class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times

        vote = Counter()
        self.maximum = []
        
        maxx = 0
        for i in persons:
            vote[i] += 1
            if vote[i] >= maxx:
                self.maximum.append(i)
                maxx = vote[i]
            else:
                self.maximum.append(self.maximum[-1])
        
        
    def q(self, t: int) -> int:
        index = bisect_right(self.times, t)

        return self.maximum[index-1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)