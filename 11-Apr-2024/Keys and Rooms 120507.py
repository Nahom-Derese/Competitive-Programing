# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        total_rooms = len(rooms)
        visited = [0] * len(rooms)
        
        stack = [0]

        while stack:
            x = stack.pop()
            visited[x] = 1
            keys = rooms[x]
            for key in keys:
                if not visited[key]:
                    stack.append(key)
        
        return sum(map(int, visited)) == total_rooms