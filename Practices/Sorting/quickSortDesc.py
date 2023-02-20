def partition(a):
    pivot = a[0]
    index = 0

    for i in range(1, len(a)):
        if a[i] > pivot:
            a[i], a[index + 1] = a[index + 1], a[i]
            index += 1

    a[0], a[index] = a[index], a[0]
    return index


def quickSort(a):
    if len(a) <= 1:
        return a

    pivot = partition(a)

    left = quickSort(a[:pivot])
    right = quickSort(a[pivot + 1:])

    return left + [a[pivot]] + right


array = [4, 2, 5, 9, 1, 3, 6, 8, 7]
print(quickSort(array))
