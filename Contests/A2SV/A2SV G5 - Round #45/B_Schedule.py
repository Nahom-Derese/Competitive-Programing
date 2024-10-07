def count_pairs_at_university(n, schedule):
    pairs_at_university = 0
    consecutve_pairs = 0
    started = False

    for i in range(n):
        pair = schedule[i]
        
        if pair == 1:
            if not started:
                started = True
            pairs_at_university += 1
            consecutve_pairs = 0
        else: 
            consecutve_pairs += 1
            if started:
                if consecutve_pairs < 2 and i + 1 < n:
                    pairs_at_university += schedule[i + 1]
                    
    return pairs_at_university 

n = int(input())
schedule = list(map(int, input().split()))

result = count_pairs_at_university(n, schedule)
print(result)