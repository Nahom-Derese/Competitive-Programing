x = input()
y = ""
for i in x:
    if i.isupper():
        y += i.lower()


print(y)