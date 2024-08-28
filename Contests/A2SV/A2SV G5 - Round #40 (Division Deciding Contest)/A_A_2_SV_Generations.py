n = int(input())

years = [int(i) for i in input().split()]

average = sum(years) // n

print(average)