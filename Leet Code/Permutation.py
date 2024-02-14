def permutation(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        l = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for p in permutation(xs):
                l.append([x]+p)
        return l


for p in permutation(list("abc")):
    print(p)
