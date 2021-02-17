# Indexing arrays
import numpy as np

# One dimensional array Indexing
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
print("No. of Dimensions: ", arr1.ndim)
print(arr1[0])  # Index 0 = 1
print(arr1[1])  # Index 1 = 2

# Two Dimensional Indexing
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
print("No of Dimensions: ", arr2.ndim)
# Indexing Row-wise
print(arr2[0])  # Index = row = 0 = [1, 2, 3]
print(arr2[1])  # Index = row = 1 = [4, 5, 6]
# Indexing elemen-wise
print(arr2[0, 0])  # Index = (row(1st dimension), col) = (0, 0) = 1
print(arr2[0, 1])  # Index = (row, col(2nd Dimension)) = (0, 1) = 2
print(arr2[1, 0])  # Index = (row, col) = (0, 0) = 4

# Three Dimensional Indexing
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 12, 13]]])
print(arr3)
print("No of Dimensions: ", arr3.ndim)
print(arr3[0, 1, 2])  # Index = (1st, 2nd, 3rd) = (0, 1, 2) = 6

