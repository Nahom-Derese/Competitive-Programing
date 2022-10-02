a, b = [int(i) for i in input().split()]

c = (a - 4) // 2
d = int((c**2 - 4*b)**0.5)
ans = [(c + d)//2 , (c - d)//2]
ans.sort()

print(str(ans[1]+2) + " " + str(ans[0]+2))