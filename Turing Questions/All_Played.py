

def check(n,m,list):
    maping = {}
    firstHalfofCurrentRound = []
    # Iterating through each round
    for i in range(m):
        # identifying the current round
        currentList = list[i]
        # getting the half of the current round
        half = len(currentList)//2
        # getting the first half of the current round
        FirstHalfofCurrentRound = list[i][:half]

        # for the first list
        # mapping the first half of the list to the other half of the list
        if i == 0:
            firstHalfofCurrentRound = FirstHalfofCurrentRound.copy()
            sets = set()
            # Map the first half of the list to the other half of the list
            for k in list[i][half:]:
                sets.add(k)
            for j in range(half):
                maping[list[i][j]] = sets

        else:
            # how many keys are in the first half of the list
            count = 0
            # list of the keys that are in the first half of the list
            FirstRoundFirstHalf = []
            # checking if the mapping key is in the first half of the list
            for k in maping.keys():
                if k in FirstHalfofCurrentRound:
                    count += 1
                    FirstRoundFirstHalf.append(k)

            # pass if the all keys are in the first half of the list or none of them are
            # because if all keys are in the first half of the list, the teams just swapped sides
            if count == 0 or count==half:
                pass

            else:
                e = firstHalfofCurrentRound.copy()
                # removing the players from current Round first half that are in the First Round First half of the Round
                for l in FirstRoundFirstHalf:
                    e.remove(l)

                for l in FirstRoundFirstHalf:
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