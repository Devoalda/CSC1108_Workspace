#

def largest(arr):
    biggest = arr[0]
    i = 0
    for index, item in enumerate(arr):
        if item > biggest:
            biggest = item
            i = index
    return i


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Question 1: Write an algorithm that returns the index of the first occurrence of the largest element in an "
          "array")
    print("index: " + str(largest(arr)))
    print("value: " + str(arr[largest(arr)]))


if __name__ == '__main__':
    main()
