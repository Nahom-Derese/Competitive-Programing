from bisect import bisect_left

n = int(input())

foursevens = []

def backtrack(idx, current):
    global foursevens

    sevens = current.count('7')
    fours = current.count('4')
    notZero = sevens and fours

    if notZero and sevens == fours:
        foursevens.append(int(current))
    if idx == 10:
        return

    backtrack(idx + 1, current + '4')
    backtrack(idx + 1, current + '7')

backtrack(0, '')
foursevens.sort()
print(foursevens[bisect_left(foursevens, n)])
