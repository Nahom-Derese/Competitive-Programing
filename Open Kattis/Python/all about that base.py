N = int(input())
g = []
for i in range(N):
    e = []
    a = input().split()
    i1 = a[0].lower()
    op = a[1]
    i2 = a[2].lower()
    ans = a[4].lower()
    check = [ord(j) for j in i1 + i2 + ans]
    maximum = max(check)
    minimum = min(check)

    if maximum > 57:
        maximum = maximum-87
    else:
        maximum = maximum-48

    if minimum > 57:
        minimum = minimum-87
    else:
        minimum = minimum-48

    if maximum == 1 and minimum == 1:
        maximum-=1

    for k in range(maximum+1,37):
        input1 =0 
        input2 = 0
        answer = 0

        count = len(i1)-1

        for o in i1:
            if ord(o) > 57:
                input1 += (ord(o) - 87) * (k** count)
            else:
                input1 += (ord(o) - 48) * (k** count)
            count -= 1
        count = len(i2)-1

        for p in i2:
            if ord(p) > 57:
                input2 += (ord(p) - 87) * (k** count)
            else:
                input2 += (ord(p) - 48) * (k** count)
            count -= 1
        count = len(ans)-1

        for u in ans:
            if ord(u) > 57:
                answer += (ord(u) - 87) * (k** count)
            else:
                answer += (ord(u) - 48) * (k** count)
            count -= 1

        if op == '+':
            if answer == input1 + input2:
                if k == 36:
                    e.append(chr(48))
                elif k > 9:
                    e.append(chr(k+87))
                else:
                    e.append(chr(k+48))
        if op == '-':
            if answer == input1 - input2:
                if k == 36:
                    e.append(chr(48))
                elif k > 9:
                    e.append(chr(k+87))
                else:
                    e.append(chr(k+48))
        if op == '*':
            if answer == input1 * input2:
                if k == 36:
                    e.append(chr(48))
                elif k > 9:
                    e.append(chr(k+87))
                else:
                    e.append(chr(k+48))
        if op == '/':
            if answer == input1 / input2:
                if k == 36:
                    e.append(chr(48))
                elif k > 9:
                    e.append(chr(k+87))
                else:
                    e.append(chr(k+48))

    g.append(e)

for i in g:
    if len(i) != 0:
        for j in i:
            print(j, end="")
        print()
    else:
        print("invalid")
            