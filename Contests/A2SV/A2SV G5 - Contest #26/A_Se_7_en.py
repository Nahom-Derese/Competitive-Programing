seven_multiples = []

for i in range(1, 1000):
    seven_multiples.append(str(7 * i))

def diff_calc(a, b):
    res = 0
    for i in range(len(a)):
        res += int(a[i] != b[i])
    return res

def solve():
    n = int(input())
    
    diff = []
    for num in seven_multiples:
        if len(num) == len(str(n)):
            diffrence = diff_calc(num, str(n))
            diff.append((diffrence, num))
    
    diff.sort()
    print(diff[0][1])

for _ in range(int(input())):
    solve()
