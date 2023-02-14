def partition(a):
    pivot = a[0]
    pivotIndex = 0

    # Move all elements smaller than pivot to the left of pivot
    for i in range(1, len(a)):
        if a[i] < pivot:
            # Move element to the left of pivot
            a[i], a[pivotIndex + 1] = a[pivotIndex + 1], a[i]
            # Increment pivot index
            pivotIndex += 1

    # Move pivot to its final position
    a[0], a[pivotIndex] = a[pivotIndex], a[0]
    return pivotIndex


def quickSort(a):
    # Base case
    if len(a) <= 1:
        return a

    # Get pivot index
    pivotIndex = partition(a)
    # Sort elements smaller than pivot
    left = quickSort(a[:pivotIndex])
    # Sort elements greater than pivot
    right = quickSort(a[pivotIndex + 1:])
    # Return sorted array
    return left + [a[pivotIndex]] + right


array = [4, 2, 5, 9, 1, 3, 6, 8, 7]
print(quickSort(array))
