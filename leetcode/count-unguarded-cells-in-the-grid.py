class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        ans = m*n - len(guards) - len(walls)
        if ans == 0:
            return 0
        
        walls = set(map(tuple, walls))
        guards = set(map(tuple, guards))
        seen = set()
        
        def checkWall(x,y):
            return (x, y) not in walls and (x, y) not in guards

        def see(x,y):
            itr_y = y+1
            # vertically downwards
            while checkWall(x, itr_y) and itr_y < n:
                seen.add((x, itr_y))
                itr_y += 1
            
            itr_y = y-1
            # vertically upwards
            while checkWall(x, itr_y) and itr_y > -1:
                seen.add((x, itr_y))
                itr_y -= 1
            
            itr_x = x+1
            # horizontally righwards
            while checkWall(itr_x, y) and itr_x < m:
                seen.add((itr_x, y))
                itr_x += 1
            
            itr_x = x-1
            # horizontaly leftwards
            while checkWall(itr_x, y) and itr_x > -1:
                seen.add((itr_x, y))
                itr_x -= 1

        for x,y in guards:
            see(x,y)
        
        print(seen)
        ans -= len(seen)

        return ans
