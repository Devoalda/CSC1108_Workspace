# recursive function to add first n term of the series 1+1/2 - 1/3+1/4-1/5

def sum(n):
    if n == 1:                        # base case
        return 1
    else:
        if n % 2 == 0:                 # if n is even
            return 1 / n + sum(n - 1)  # add 1/n
        else:
            return -1 / n + sum(n - 1)  # subtract 1/n


# Test cases
assert sum(1) == 1, "sum(1) should be 1, but returned " + str(sum(1))
assert sum(2) == 1.5, "sum(2) should be 1.5, but returned " + str(sum(2))
assert sum(3) == (1 + 1/2 - 1/3), "sum(3) should be 1.1666666666666667, but returned " + str(sum(3))
assert sum(4) == (1 + 1/2 - 1/3 + 1/4), "sum(4) should be 1.4166666666666667, but returned " + str(sum(4))
assert sum(5) == (1 + 1/2 - 1/3 + 1/4 - 1/5), "sum(5) should be 1.2833333333333332, but returned " + str(sum(5))

print("All tests passed!")