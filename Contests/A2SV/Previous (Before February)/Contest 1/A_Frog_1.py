n = int(input())
stones = [int(x) for x in input().split()]

def solve():
    if len(stones) == 1:
        print(0)
        return

    if len(stones) < 3:
        print(stones[1] - stones[0])    
        return

    first_stone = 0
    second_stone = abs(stones[1] - stones[0])

    for i in range(2, len(stones)):
        first_stone, second_stone = second_stone, min(first_stone + abs(stones[i] - stones[i-2]), second_stone + abs(stones[i] - stones[i-1]))
        
    print(second_stone)

solve()