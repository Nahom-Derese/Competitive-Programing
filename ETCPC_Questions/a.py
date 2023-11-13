def splitter(list):
    Sptr = 0
    Eptr = len(b)-1

    while list[Sptr] != 0:
        if(Sptr > len(b)-1):
            break
        else:
            Sptr += 1

    if(Sptr != len(b)-1):
        Eptr = Sptr + 1

    while list[Eptr] != 0:
        if(Eptr == len(b) - 1):
            break
        else:
            Eptr += 1

    return list[Sptr+1:Eptr]












a = input()
b = [int(x) for x in input().split()]

# for i in range(5):
#     print(b)
#     minimum = min(b)

#     if (minimum < 0):
#         b = [x+abs(minimum) for x in b]

#     else:
#         b = [x-abs(minimum) for x in b]


#     b = splitter(b)

#     print(b)

c = ' '.join(str(x) for x in b).split('0')
s = []
for k in c:
    k = k.strip()
    if k == '':
        continue
    
    s += [int(x) for x in k.split(' '))]

print(s)
# print(b)