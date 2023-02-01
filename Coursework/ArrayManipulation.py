#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
#Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.

def arrayManipulation(n, queries):
    # Write your code here
    # create an array of zeros
    arr = [0] * (n + 1)
    sum = 0
    max = 0
    # iterate through queries
    for i in range(len(queries)):
        # get the start and end indices
        start = queries[i][0]
        end = queries[i][1]
        # get the value to add
        value = queries[i][2]
        # add the value to the start index
        arr[start] += value
        # subtract the value from the end index + 1
        if end + 1 <= n:
            arr[end + 1] -= value
    # iterate through the array
    for i in range(1, len(arr)):
        # add the value at the current index to the sum
        sum += arr[i]
        # if the sum is greater than the max, set the max to the sum
        if sum > max:
            max = sum
    # return the max
    return max


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()


# Sample Input
#
# 5 3
# 1 2 100
# 2 5 100
# 3 4 100
# Sample Output
#
# 200