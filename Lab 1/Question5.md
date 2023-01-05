# Question 5
An algorithm for finding the maximum element of an array is in the following
```python
def arrayMax(a,n):
    currentMax = a[0]
    for i in range(1,n):
        if a[i] > currentMax:
            currentMax = a[i]
    return currentMax
```

Determine the number of times that the statement "currentMax = a[i]" will be
executed in the best case and in the worst case.

The best case is when the array is already sorted in ascending order. In this case, the statement "currentMax = a[i]" will be executed only once, when i = 0. 

The worst case is when the array is sorted in descending order. In this case, the statement "currentMax = a[i]" will be executed n-1 times, when i = 1, 2, ..., n-1.