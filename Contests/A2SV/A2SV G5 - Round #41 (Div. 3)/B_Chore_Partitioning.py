n, a, b = [int(i) for i in input().split()]

complexities = [int(i) for i in input().split()]
complexities.sort()

print(complexities[-a] - complexities[-a-1])