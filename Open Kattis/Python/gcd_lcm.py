import math

def find_pairs(x, y):
    gcd = math.gcd(x, y)
    lcm = (x * y) // gcd

    pairs = []
    for i in range(1, int(math.sqrt(lcm)) + 1):
        if lcm % i == 0:
            j = lcm // i
            if math.gcd(i, j) == x:
                pairs.append((i, j))
                if i != j:
                    pairs.append((j, i))

    pairs.sort()

    return pairs

# Read input values
x, y = map(int, input().split())

# Find and print the pairs
pairs = find_pairs(x, y)
for pair in pairs:
    print(pair[0], pair[1])
