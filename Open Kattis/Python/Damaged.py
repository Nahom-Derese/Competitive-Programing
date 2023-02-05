from itertools import product 

a = [int(i) for i in input().split()]

def calc(x, y, operator):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == '/':
        try:
            return int(x / y)
        except ZeroDivisionError:
            return None

ans = []

for i in product('+-*/', repeat= 2):
    c = calc(a[0], a[1], i[0])
    d = calc(a[2], a[3], i[1])
    if c is None:
        continue
    if d is None:
        continue
    if c == d:
        ans.append(f"{a[0]} {i[0]} {a[1]} = {a[2]} {i[1]} {a[3]}")

ans.sort(key=lambda item: (item.split()[1], item.split()[5]))

if len(ans) == 0:
    print("problems ahead")
for i in ans:
    print(i)
        
    

