# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0

        def bfs_by_level(start):
            visited = set()
            queue = deque(start)
            visited.update(start)
            level = 1
            while queue:
                level_size = len(queue)
                current_level = []
                for _ in range(level_size):
                    node = queue.popleft()
                    current_level.append(node)
                    if node == amount:
                        return level
                    for neighbor in coins:
                        if neighbor+node not in visited:
                            if neighbor+node > amount:
                                continue
                            visited.add(node+neighbor)
                            queue.append(node+neighbor)
                level += 1
                
            return -1

        return bfs_by_level(coins)
