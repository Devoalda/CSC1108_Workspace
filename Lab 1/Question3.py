def smallesttwo(arr):
    small = arr[0]
    small2 = arr[0]
    for item in arr:
        if item < small:
            small = item
    for item in arr:
        if item < small2 and item != small:
            small2 = item

    return small, small2

def main():
    print("Question 3: Write an algorithm that output the smallest and the second smallest values in the array s[0],"
          "…s[n-1]. Assume that n>1 and the values in the array are distinct.")
    arr = [9, 2, 4, 5, 6, 7, 8, 3, 10]
    small, small2 = smallesttwo(arr)
    print("Smallest: " + str(small))
    print("Second Smallest: " + str(small2))


if __name__ == '__main__':
    main()
