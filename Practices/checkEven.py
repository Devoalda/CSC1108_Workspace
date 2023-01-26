
# Checking if a value is an even number or not


def checkEven(n):
    return n & 1 == 0


assert checkEven(2) == True, "checkEven(2) should be True, but returned " + str(checkEven(2))
assert checkEven(3) == False, "checkEven(3) should be False, but returned " + str(checkEven(3))

print("All tests passed!")