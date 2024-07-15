def points(p, t):
    return max((3 * p) / 10, p - (p*t/250))

a, b, c, d = [int(i) for i in input().split()]

Misha = points(a, c)
Vasya = points(b, d)

if Misha > Vasya:
    print("Misha")
elif Misha < Vasya:
    print("Vasya")
else:
    print("Tie")