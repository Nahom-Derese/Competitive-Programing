for i in range(int(input())):
    stones = [int(x) for x in input()]

    if len(stones) == 1:
        print(0)
        continue
    
    if len(stones) < 3:
        print(stones[0])    
        continue

    first_stone = 0
    second_stone = abs(stones[1] - first_stone)

    for i in range(2, len(stones)):
        first_stone, second_stone = second_stone, min(first_stone + abs(stones[i] - stones[i-1]), second_stone + abs(stones[i] - stones[i-2]))
    
    print(second_stone)