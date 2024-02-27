count = set()

def divide(n, a, b):
    count.add(n)
    if n > 1 and n % a == 0:
        divide(n//a, a, b)
    if n > 1 and n % b == 0:
        divide(n//b, a, b)

for i in range(int(input())):
    count = set()
    a,b,l = map(int, input().split())


    if l % a != 0 and l % b != 0:
        print(1)
    else:
        divide(l, a, b)
        print(len(count))

    
