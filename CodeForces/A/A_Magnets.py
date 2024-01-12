x = int(input())

s = []

for i in range(x):
    s.append(int(input()[0]))

ptr = 1
ans=1

while ptr < len(s):
    if s[ptr] != s[ptr-1]:
        ans += 1
    ptr+=1

print(ans)    