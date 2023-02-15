
def selSort(a):
    for i in range(len(a)):
        minIndex = i
        for j in range(i + 1, len(a)):
            if a[j] < a[minIndex]:
                minIndex = j
            a[i], a[minIndex] = a[minIndex], a[i]

    return a

def selSortMax(a):
    # For each element in the array starting from the end
    for i in range(len(a) - 1, 0, -1):
        maxIndex = i
        # Search for max element in the array from the beginning
        for j in range(i):
            if a[j] > a[maxIndex]:
                maxIndex = j
            # Swap the max element with the last element
            a[i], a[maxIndex] = a[maxIndex], a[i]

    return a

array = [4, 2, 5, 9, 1, 3, 6, 8, 7]
selSort(array)
selSortMax(array)
print(array)

