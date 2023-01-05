def reverse(arr):
    arr_tmp = []
    for i in range(len(arr)):
        arr_tmp.append(arr[len(arr) - 1 - i])
    return arr_tmp


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Question 2: Write an algorithm that reverses the array")
    print(reverse(arr))


if __name__ == '__main__':
    main()
