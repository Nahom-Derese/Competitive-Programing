from collections import Counter

n,k = [int(i) for i in input().split()]

freq = Counter()

for letter in range(ord("A"), ord("A")+k):
    freq[chr(letter)] = 0

for char in input():
    freq[char] += 1

print(min(freq.values()) * k)