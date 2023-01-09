def callpoints(ops):
    points = 0
    ans = []
    for op in ops:
        if op == 'C':
            ans.pop()
        elif op == 'D':
            ans.append(ans[-1] * 2)
        elif op == '+':
            ans.append(sum(ans[-2:]))
        else:
            ans.append(int(op))
    return sum(ans)

print(callpoints(["5","-2","4","C","D","9","+","+"]))