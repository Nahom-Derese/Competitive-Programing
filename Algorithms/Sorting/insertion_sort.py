

def insertionSort(unsorted):
    for i in range(1, len(unsorted)):
        j = i
        while j != 1 and unsorted[i] <= unsorted[j]:
            j-=1
        unsorted[j], unsorted[i] = unsorted[i], unsorted[j]

    return unsorted


print(insertionSort([3, 0, 2, -5, 10, 2]))