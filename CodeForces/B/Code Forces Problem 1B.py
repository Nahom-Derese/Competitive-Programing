from itertools import permutations

a = int(input())


for i in range(a):
    b = int(input())

    c = permutations(range(1, b+1), b)
    
    d = list(c)
        
    print(" ".join(str(d[0])))


