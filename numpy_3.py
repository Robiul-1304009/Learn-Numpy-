# Slicing Arrays

import numpy as np

# Slicing one dimensional array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1[0:3])  # Index = 0, 1, 2 = 1, 2, 3
print(arr1[2:5])  # Index = 2, 3, 4 = 3, 4, 5
print(arr1[:])    # Index = whole array(0:5) = 1-5
print(arr1[1:])    # Index = 1-Last = array(1:5) = 2-5
print(arr1[:4])    # Index = 0-3 = whole array(0:4) = 1, 2, 3
print(arr1[:4:2])  # Index = 0-3 with steps 2 = 0, 2 = 1, 3

# Slicing Two dimensional array
arr2 = np.array([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
print(arr2[1, 0:2])  # index = rows(1st dimension) = [3, 4, 5]
# slice(0:2) = 0, 1 = 3, 4
print(arr2[0:2, 0])  # Index = rows 0, 1 = [1, 2, 3] [3, 4, 5]
# find first element of arrays(0) = 1, 3
print(arr2[0:2, 0:2])  # slicing the arrays = 0, 1 = 1 2 3 4

