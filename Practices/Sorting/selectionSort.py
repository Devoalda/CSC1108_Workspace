
def selSort(a):
    for i in range(len(a)):
        minIndex = i

        for j in range(i+1, len(a)):
            if a[j] < a[minIndex]:
                minIndex = j
            print(a)
        a[i], a[minIndex] = a[minIndex], a[i]

array = [4, 2, 5, 9, 1, 3, 6, 8, 7]
selSort(array)









#    for i in range(len(a)):
#        min = i
#        for j in range(i+1, len(a)):
#            if a[j] < a[min]:
#                min = j
#        a[i], a[min] = a[min], a[i]
















