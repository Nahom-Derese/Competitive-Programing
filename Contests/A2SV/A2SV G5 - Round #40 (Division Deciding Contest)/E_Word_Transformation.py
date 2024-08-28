import string
from collections import Counter

def solve():
    main, sub = [list(i) for i in input().split()]

    main_count = Counter(main)
    sub_count = Counter(sub)

    for i in string.ascii_uppercase:
        while main_count[i] > sub_count[i]:
            main.remove(i)
            main_count[i]-=1
    
    if main == sub:
        return "YES"
    return "NO"

for _ in range(int(input())):
    print(solve())