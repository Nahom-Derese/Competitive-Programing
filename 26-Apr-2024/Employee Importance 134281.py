# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        graph = defaultdict(list)

        for employee in employees:
            graph[employee.id].append(employee.importance)
            graph[employee.id].append(employee.subordinates)

        def dfs(node):
            summ = 0
            for sub in graph[node][1]:
                summ += dfs(sub)
            return graph[node][0] + summ

        return dfs(id)