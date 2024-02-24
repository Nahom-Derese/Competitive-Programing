a = input()

def removeDuplicate(string):
    if len(string) < 2:
        return string
    
    ans = string
    for i in range(1, len(string)):
        if string[i-1] == string[i]:
            ans = string[:i-1] + string[i+1:]
            break
    else:
        print(ans)
        exit()  
removeDuplicate(a)