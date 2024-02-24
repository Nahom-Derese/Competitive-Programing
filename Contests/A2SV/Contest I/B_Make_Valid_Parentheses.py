exp = input()

stack = []

for i in exp:
    if i == '(':
        stack.append(i)
    else:
        if stack and stack[-1]=='(':
            stack.pop()
        else:
            stack.append(i)

print(len(exp)-len(stack))