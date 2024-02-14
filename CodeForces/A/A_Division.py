
t = int(input())
for i in range(t):
    n = int(input())
    
    if n >= 1900:
        print("Division 1")
    elif n >= 1600 and n < 1900:
        print("Division 2")
    elif n >= 1400 and n < 1600:
        print("Division 3")
    elif n < 1400:
        print("Division 4")


