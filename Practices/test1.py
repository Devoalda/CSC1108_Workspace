def partition(a):
    pivot = a[0]
    pivotIndex = 0

    for i in range(1, len(a)):
        if a[i] < pivot:
            a[i], a[pivotIndex + 1] = a[pivotIndex + 1], a[i]
            pivotIndex += 1

    a[0], a[pivotIndex] = a[pivotIndex], a[0]
    return pivotIndex

# Using partition to find 0 to kth smallest element
# Without using quickSort
# Obfuscate this line
def findKthsmallest(nums, k): print(nums[:partition(nums)][::-1])
    #partition(nums)
    #for i in range(k):
    #    if i == k - 1:
    #        print(nums[i])
    #    else:
    #        print(nums[i], end=", ")

    # 1 line partition to find 0 to kth smallest element and reverse

def quickSort(a):
    if len(a) <= 1:
        return a
    pivotIndex = partition(a)
    left = quickSort(a[:pivotIndex])
    right = quickSort(a[pivotIndex + 1:])
    return left + [a[pivotIndex]] + right


def findKthLargest(nums, k):
    sortedArray = quickSort(nums)
    for i in range(k):
        print(sortedArray[i])

def binarySerarchK(nums,k):
    left = 0
    right = len(nums) - 1

    # Return element 1 to k
    while left <= right:
        mid = (left + right) >> 1
        if mid == k:
            return nums[:mid]
        elif mid < k:
            left = mid + 1
        else:
            right = mid - 1
    return -1

array = [4, 2, 5, 9, 1, 3, 6, 8, 7]
findKthsmallest(array, 3)
print(quickSort(array))
