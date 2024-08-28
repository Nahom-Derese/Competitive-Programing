def solve():
    n = int(input())
    s = list(input())

    stack = [(s[0], 0)]

    for i in range(1, n):
        if stack and stack[-1][0] >= s[i]:
            stack.pop()
            stack.append((s[i], i))
    
    x = s.pop(stack[-1][1])
    s.insert(0, x[0])
    print("".join(s))

for _ in range(int(input())):
    solve()
