ans = ""
sett = set(["A", "O", "Y", "E", "U", "I"])
for i in input():
    if i.upper() not in sett:
        ans+="."+i.lower()
print(ans)