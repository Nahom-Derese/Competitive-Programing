# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        tasks = sorted([task + [index] for index, task in enumerate(tasks)], reverse=True)
        print(tasks)        
        queue = []

        ans = []
        time = tasks[-1][0]
        while tasks or queue:
            if not queue:
                if tasks:
                    temp = tasks[-1][0]
                    while tasks and tasks[-1][0] == temp:
                        psT, pT, i = tasks.pop()
                        time = psT
                        heappush(queue, [pT, i, psT, 0])
        
            
            x = heappop(queue)
            processTime, index, startTime , _= x
            time+= processTime
            
            ans.append(index)
            
            while tasks and tasks[-1][0] <= time:
                psT, pT, i = tasks.pop()
                heappush(queue, [pT, i, psT, 0])
            
        

        return ans