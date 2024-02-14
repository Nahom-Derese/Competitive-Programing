import string

alpha = string.ascii_lowercase

for i in range(int(input())):
    a, b = [int(i) for i in input().split()]

    print(alpha[:b]*a)