# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for course1, course2 in prerequisites:
            graph[course1].append(course2)
            indegree[course2]+=1


        def topsort(multisource):
            res = [set() for _ in range(numCourses)]
            queue = deque(multisource)

            while queue:
                x = queue.popleft()

                for node in graph[x]:
                    indegree[node]-=1
                    
                    # give previous ancestors to the child
                    res[node].add(x)
                    res[node].update(res[x])

                    if indegree[node]:
                        continue
                    queue.append(node)
                    
            return res


        multi_source = [i for i in range(numCourses) if not indegree[i]]

        course_topology = topsort(multi_source)
        return[a in course_topology[b] for a, b in queries]