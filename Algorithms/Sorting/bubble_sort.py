def bubbleSort(unsorted):
    for i in range(len(unsorted)):
        for j in range(1, len(unsorted)-i):
            if unsorted[j-1] > unsorted[j]:
                unsorted[j-1], unsorted[j] = unsorted[j], unsorted[j-1]

    return unsorted


print(bubbleSort([3, 0, 2, -5, 10, 2]))