def merge(array1, array2):
    array3 = []
    size1 = len(array1)
    size2 = len(array2)

    index1 = index2 = 0

    while index1 < size1 and index2 < size2:
        if array1[index1] < array2[index2]:
            array3.append(array1[index1])
            index1 += 1
        else:
            array3.append(array2[index2])
            index2 += 1

    for i in range(index1, size1):
        array3.append(array1[i])

    for i in range(index2, size2):
        array3.append(array2[i])

    return array3


def mergeSort(array):
    size = len(array)
    if size <= 1:
        return array

    mid = size // 2

    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])

    return merge(left, right)


array = [4, 2, 5, 9, 1, 3, 6, 8, 7]
print(mergeSort(array))
