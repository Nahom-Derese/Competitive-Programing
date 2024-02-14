i = input()

def x (i):
    d = [4,7,44,47,74,77,444,447,474,477,744,747,774,777]

    if int(i) in d:
        return "YES"

    else:
        for j in range(len(d)):
            if int(i) % d[j] == 0:
                return "YES"
    return 'NO'


print(x(i))