def partition(a):
    pivot = a[0]
    pivotIndex = 0

    for i in range(1, len(a)):
        if a[i] < pivot:
            a[i], a[pivotIndex + 1] = a[pivotIndex + 1], a[i]
            pivotIndex += 1

    a[0], a[pivotIndex] = a[pivotIndex], a[0]
    return pivotIndex


def quickSort(a):
    if len(a) <= 1:
        return a
    pivotIndex = partition(a)
    left = quickSort(a[:pivotIndex])
    right = quickSort(a[pivotIndex + 1:])
    return left + [a[pivotIndex]] + right


array = [4, 2, 5, 9, 1, 3, 6, 8, 7]
print(quickSort(array))
