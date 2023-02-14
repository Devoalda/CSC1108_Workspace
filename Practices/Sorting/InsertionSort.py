def insertionSort(a):
    for i in range(1, len(a)):
        currentValue = a[i]
        position = i

        while position > 0 and a[position - 1] > currentValue:
            a[position] = a[position - 1]
            position -= 1
        a[position] = currentValue

        print(a)


array = [4, 2, 5, 9, 1, 3, 6, 8, 7]
insertionSort(array)

# Output
# [2, 4, 5, 9, 1, 3, 6, 8, 7]
# [2, 4, 5, 9, 1, 3, 6, 8, 7]
# [2, 4, 5, 9, 1, 3, 6, 8, 7]
# [1, 2, 4, 5, 9, 3, 6, 8, 7]
# [1, 2, 3, 4, 5, 9, 6, 8, 7]
# [1, 2, 3, 4, 5, 6, 9, 8, 7]
# [1, 2, 3, 4, 5, 6, 8, 9, 7]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

