while True:
    a = int(input())
    r = 0
    if a == -1:
        break
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            print(f"{a} is COMPOSITE TT")
            break
        elif i == int(a**0.5):
            print(f"{a} is PRIME!!")
