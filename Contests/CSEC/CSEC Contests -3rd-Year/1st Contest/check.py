r = ''

k = int(input())

ans = []
# for i in range(1, 100):
#     for j in range(1, i+1):
#         r += str(j)
for i in range(2, k+2):
    ans.append(len(r))
    for j in range(1, i):
        r += str(j)

# for i in range(k-10, k+8):
#     print(i, end="    ")

# print()

# for i in range(k-9, k+9):
#     print(f"   {r[i]}", end=" ")

# print(len(r))
# print(r)

ans = ans[1:]

print(ans)
