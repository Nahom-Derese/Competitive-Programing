a = input()
op = input()
b = input()

if(a == '0' or b == '0'):
    print('0')
else:
    if op == '+':
        if len(a) > len(b):
            t = list(a)
            t[len(a)-len(b)] = '1'
            print(''.join(t))
        else:
            t = list(b)
            if b[len(b)-len(a)] == '0':
                t[len(b)-len(a)] = '1'
            else:
                t[len(b)-len(a)] = '2'
            print(''.join(t))

    elif op == '*':
        c = list(a)
        c.append('0'*(len(b)-1))
        print(''.join(c))
