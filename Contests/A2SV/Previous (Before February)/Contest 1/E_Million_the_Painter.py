_ = int(input())

s = input()

for i in range(1, len(s)):
    if s[i] == s[i - 1] and s[i] != "?":
        print("No")
        break
else:
    if s[0] == "?" or s[-1] == "?":
        print("Yes")
    elif ("??" in s) or ("C?C" in s) or ("Y?Y" in s) or ("M?M" in s):
        print("Yes")
    else:
        print("No")