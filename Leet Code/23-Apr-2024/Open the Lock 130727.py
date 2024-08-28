# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        graph = {
            '0' : ('1','9'),
            '1' : ('2','0'),
            '2' : ('3','1'),
            '3' : ('4','2'),
            '4' : ('5','3'),
            '5' : ('6','4'),
            '6' : ('7','5'),
            '7' : ('8','6'),
            '8' : ('9','7'),
            '9' : ('0','8')
        }

        def neighbour(string):
            string = list(string)
            for i in range(len(string)):
                for n in graph[string[i]]:
                    x = string[i]
                    string[i] = n
                    yield "".join(string)
                    string[i] = x

        def bfs():
            queue = deque(["0000"])
            visited = set(["0000"])
            
            level = 0
            while queue:
                boundary = len(queue)

                for _ in range(boundary):
                    pincode = queue.popleft()
                    if pincode == target:
                        return level
                    
                    if pincode not in deadends:
                        for next_pincode in neighbour(pincode):
                            if next_pincode not in visited:
                                visited.add(next_pincode)
                                queue.append(next_pincode)
                level+=1
            
            return -1

        return bfs()
        