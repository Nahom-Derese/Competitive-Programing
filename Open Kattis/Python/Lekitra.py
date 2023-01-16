word = input()

ASCII = [ord(i)-96 for i in word]
ASCIISORTED = sorted(ASCII)
minimumIndex = ASCII.index(ASCIISORTED[0])

ans = []
c = 0
i = 0
while i in range(3):
    if i == 2:
        ans = ans + list(word[::-1])
        break
    if minimumIndex <= len(word)-3+c:
        ans = ans + list(word[:minimumIndex+1][::-1])
        word = word[minimumIndex+1:]
        ASCII = ASCII[minimumIndex+1:]
        ASCIISORTED = sorted(ASCII)
        minimumIndex = ASCII.index(ASCIISORTED[0])
    else:
        c+=1
        i-=1
        minimumIndex = ASCII.index(ASCIISORTED[c])
    c+=1
    i+=1
    

print("".join(ans))
