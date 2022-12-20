

def check(n,m,list):
    maping = {}
    firsthalfcurrentList = []
    for i in range(len(list)):
        currentList = list[i]
        half = len(currentList)//2
        halfcurrentList = list[i][:half]

        # for the first list
        # mapping the first half of the list to the other half of the list
        if i == 0:
            firsthalfcurrentList = halfcurrentList.copy()
            sets = set()
            for k in list[i][half:]:
                sets.add(k)
            for j in range(half):
                maping[list[i][j]] = sets

        else:
            # how many keys are in the first half of the list
            count = 0
            # list of the keys that are in the first half of the list
            listing = []
            # checking if the mapping key is in the first half of the list
            for k in maping.keys():
                if k in halfcurrentList:
                    count += 1
                    listing.append(k)

            # pass if the all keys are in the first half of the list or none of them are
            if count == 0 or count==half:
                pass

            else:
                
                e = firsthalfcurrentList.copy()
                for l in listing:
                    e.remove(l)

                for l in listing:
                    for w in e:
                        s = maping[l].copy()
                        s.add(w)
                        s2 = maping[w].copy()
                        s2.add(l)
                        maping[l] = s
                        maping[w] = s2

    # checking if the mapping is full
    count = 0
    for k in maping.keys():
        if len(maping[k]) == n-1:
            count += 1
    if count == n/2:
        return True
    else:
        return False
    
print(check(2, 1, [[1, 2]]))
print(check(4, 2, [[1, 2, 3, 4], [4, 3, 1, 2]]))
print(check(4, 2, [[1, 2, 3, 4], [1, 3, 2, 4]]))
print(check(6, 6, [[1, 6, 3, 4, 5, 2], [6, 4, 2, 3, 1, 5], [4, 2, 1, 5, 6, 3], [4, 5, 1, 6, 2, 3], [3, 2, 5, 1, 6, 4], [2, 3, 6, 4, 1, 5]]))
print(check(6, 6, [[3, 1, 4, 5, 6, 2], [5, 3, 2, 4, 1, 6], [5, 3, 6, 4, 2, 1], [6, 5, 3, 2, 1, 4], [5, 4, 1, 2, 6, 3], [4, 1, 6, 2, 5, 3]]))