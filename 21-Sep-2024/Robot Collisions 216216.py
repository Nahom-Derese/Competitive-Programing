# Problem: Robot Collisions - https://leetcode.com/problems/robot-collisions/

class Solution:


    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = list(map(list, list(zip(positions, healths, directions, range(1, len(positions)+1)))))
        robots.sort()

        print(robots)

        stack = []

        for robot in robots:
            if stack:
                
                if robot[2] == "L":
                    add = True
                    while stack and stack[-1][2] == "R" and add:
                        last_health = stack[-1][1]
                        if robot[1] > last_health:
                            stack.pop()
                            robot[1] -= 1
                        elif robot[1] < last_health:
                            stack[-1][1] -= 1
                            add = False
                        else:
                            stack.pop()
                            add = False

                    if add:
                        stack.append(robot)
                else:
                    stack.append(robot)

            else:
                stack.append(robot)

        stack.sort(key=lambda x: x[3])

        return map(lambda x: x[1], stack)