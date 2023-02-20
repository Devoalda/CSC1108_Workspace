# question 4
def orderInsert(a, value):
    # remove pass
    left = 0
    right = len(a) - 1

    while left <= right:
        mid = (left + right) >> 1
        if a[mid] == value:
            a.insert(mid, value)
            return
        elif a[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    a.insert(left, value)


array = input("Enter a list of numbers in increasing order separated by commas:\n")
array = [int(x) for x in array.split(",")]

number = input("Enter a number to be inserted into the array:\n")

orderInsert(array, int(number))
print(array)