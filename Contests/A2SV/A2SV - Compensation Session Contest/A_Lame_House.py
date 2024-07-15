boring = []
boring_str = []
for i in range(1, 10):
    for j in range(1, 5):
        num = str(i) * j
        if int(num) < 10000:
            boring.append(int(num))
            boring_str.append(num)


def solve():
    x = int(input())

    u = boring.index(x) + 1
    ans = 0
    for i in range(u):
        ans += len(boring_str[i])


    return ans    

for _ in range(int(input())):
    print(solve())