from math import factorial

m = int(input())

baloons = [int(i) for i in input().split()]

print(factorial(len(set(baloons))))