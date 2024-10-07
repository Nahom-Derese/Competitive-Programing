# def solve():
#     n, k = [int(i) for i in input().split()]
    
#     if k >= n:
#         return 1
    
#     x = int(n ** 0.5)
#     for i in range(2, min(x, k)+1):
#         if n % i == 0 and (n // i) <= k:
#             return min(i, n // i)
    
#     return n

# for _ in range(int(input())):
#     print(solve())

def solve():
    n, k = [int(i) for i in input().split()]

    if k >= n:
        return 1

    x = int(n ** 0.5)
    for i in range(2, min(x, k)+1):
        if n % i == 0 and (n // i) <= k:
            return i


    return n

for _ in range(int(input())):
    print(solve())