# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        InDegrees = [0 for i in range(numCourses)]

        for course, pre in prerequisites:
            InDegrees[course]+=1
            graph[pre].append(course)

        ans = []
        def bfs(node):
            queue = deque([node])

            while queue:
                currentLevel = len(queue)

                for _ in range(currentLevel):
                    node = queue.popleft()
                    ans.append(node)
                    for neighbour in graph[node]:
                        InDegrees[neighbour]-=1
                        if InDegrees[neighbour]:
                            continue
                        queue.append(neighbour)
            

        for node in [i for i in range(numCourses) if not InDegrees[i]]:
            bfs(node)
        if len(ans) != numCourses:
            return []
        return ans