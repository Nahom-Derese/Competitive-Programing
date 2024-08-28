a = int(input())

answer = []

for i in range(a):
    b = input()
    o = 0
    c = 0
    for i in b:
        if i == 'X':
            c = 0
            continue
        c += 1
        o += c
    answer.append(o)

print(*answer, sep='\n')
