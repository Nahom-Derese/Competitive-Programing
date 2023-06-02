r = ''

k = int(input())

ans = []

for i in range(2, k+2):
    ans.append(len(r))
    for j in range(1, i):
        r += str(j)


ans = ans[1:]

# print(ans)
st = ""
for i in range(1, len(ans)):
    st += str(ans[i]) + " "

print(st[ans[-2] - k])
