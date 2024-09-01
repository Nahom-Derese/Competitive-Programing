def deletion_distance(str1: str, str2: str) -> int:
    N = len(str1)
    M = len(str2)

    cache = {}


    def dp(i1, i2):
        if (i1, i2) in cache:
            return cache[(i1, i2)]

        if i1 == N:
            cache[(i1, i2)] = M - i2
            return cache[(i1, i2)]
        
        if i2 == M:
            cache[(i1, i2)] = N - i1
            return cache[(i1, i2)]

        if str1[i1] == str2[i2]:
            cache[(i1, i2)] = dp(i1+1, i2+1)
            return cache[(i1, i2)]

        else:
            cache[(i1, i2)] = min(
                dp(i1+1, i2),
                dp(i1, i2+1)
                ) + 1
                
            return cache[(i1, i2)]
    
    return dp(0,0)


print(deletion_distance("c", ""))