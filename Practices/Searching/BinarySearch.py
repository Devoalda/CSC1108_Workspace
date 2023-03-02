def iterativeBinarySearch(array, value):
    left = 0
    right = len(array)

    while left <= right:
        mid = (left + right) >> 1
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binarySearchWithForLoop(array, value):
    left = 0
    right = len(array)

    for i in range(len(array)):
        mid = (left + right) >> 1
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def recursiveBinarySearch(array, value, left, right):
    if left > right:
        return -1

    mid = (left + right) >> 1
    if array[mid] == value:
        return mid
    elif array[mid] < value:
        return recursiveBinarySearch(array, value, mid + 1, right)
    else:
        return recursiveBinarySearch(array, value, left, mid - 1)


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(iterativeBinarySearch(array, 10))
print(recursiveBinarySearch(array, 4, 0, len(array) - 1))
print(binarySearchWithForLoop(array, 5))
