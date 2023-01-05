def main():
    print("Question 4: Given an array s[0],…,s[n-1] such that n > 1 and s[i] ≤ s[i+1] for all i. Write an "
          "algorithm that inserts an input value x into the array so that s[i] ≤ s[i+1] for all i.")

    arr = []
    i = int(input("Enter size of array: "))

    while i > 0:
        x = int(input("Enter a number: "))
        if arr:
            if x >= arr[len(arr) - 1]:
                arr.append(x)
                i -= 1
            else:
                print("Number must be greater than or equal to the last number in the array")

        else:
            arr.append(x)

    print(arr)


if __name__ == '__main__':
    main()
