import sys

n = int(sys.stdin.readline().strip())

x,y = [int(i) for i in sys.stdin.readline().split()]

plates_1 = [int(i) for i in sys.stdin.readline().split()]
plates_2 = [int(i) for i in sys.stdin.readline().split()]

l = r = my_plates = minutes = 0

while l < x and r < y:
    if  my_plates == n:
        break
    if plates_1[l] < plates_2[r]:
        my_plates+= plates_1[l] == 0
        l+=1

    elif plates_1[l] > plates_2[r]:
        my_plates+= plates_2[r] == 0
        r+=1
    
    else:
        my_plates+= plates_2[r] == 0
        l+=1
    minutes+=1

if l == x:
    while r < y and my_plates < n:
        my_plates+= plates_2[r] == 0
        r+=1
        minutes+=1

if r == y:
    while l < x and my_plates < n:
        my_plates+= plates_1[l] == 0
        l+=1
        minutes+=1


if my_plates == n:
    print("YES")
    print(minutes)
else:
    print("NO")


def pow_two(n):
    return n & (n - 1) == 0
