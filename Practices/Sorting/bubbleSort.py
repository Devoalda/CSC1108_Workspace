
def bubbleSort(a):
    count = 0
    for item in range(0, len(a)):
        for i in range(0, len(a) - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]

            print(a)

    print("Number of swap for each item:", count)



array = [9,8,7,6,5,4,3,2,1]
bubbleSort(array)
