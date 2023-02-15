def bubbleSort(a):
    for i in range(len(a)):
        # -i because the last i elements are already sorted
        # -1 because we compare j and j+1
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

array = [3,4,2,9,5,1,6]
bubbleSort(array)
print(array)
