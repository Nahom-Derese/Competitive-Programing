year = input()

def checkYear(string):
    return len(set(string)) == 4

for i in range(int(year)+1, 10000):
    if checkYear(str(i)):
        print(i)
        break
