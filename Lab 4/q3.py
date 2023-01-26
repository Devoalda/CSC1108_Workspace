# def GCD(n, m):
#     if m <= n and n % m == 0:       # base case
#         return m
#     elif n < m:                     # if n < m, swap n and m
#         return GCD(m, n)
#     else:
#         return GCD(m, n % m)        # recursive call to find gcd with n % m




def GCD(n,m):
  # remove pass and insert your code here
  # for hte purpose of this exercise you should
  # call the function GCD() with a smaller value of
  # the parameters appropriately.
    if m <= n and n % m == 0:
        return m
    elif n < m:
        return GCD(m, n)
    else:
        return GCD(m, n % m)

n1 = int(input("Enter the first number:\n"))
n2 = int(input("Enter the second number:\n"))    

print("The GCD of", n1, "and", n2, "is", GCD(n1,n2))

# Test cases
assert GCD(12, 8) == 4, "GCD(12, 8) should be 4, but returned " + str(GCD(12, 8))
assert GCD(8, 12) == 4, "GCD(8, 12) should be 4, but returned " + str(GCD(8, 12))
assert GCD(12, 9) == 3, "GCD(12, 9) should be 3, but returned " + str(GCD(12, 9))
assert GCD(9, 12) == 3, "GCD(9, 12) should be 3, but returned " + str(GCD(9, 12))

print("All tests passed!")
