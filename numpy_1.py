# Creating arrays and Dimensional Arrays

import numpy as np
# Creating a array
array = np.array([1, 2, 3, 4, 5])
print(array)

# Explore different size dimension
# Zero Dimensional Array
zero_dim = np.array(31243154)
print(zero_dim)

# One Dimensional Array
one_dim = np.array([1, 2, 3])
print(one_dim)

# Two Dimensional Array
two_dim = np.array([[1, 2, 3], [4, 5, 6]])
print(two_dim)

# Three Dimensional Array
three_dim = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(three_dim)

# Find dimension of given array
print("Number of Dimensions: ", three_dim.ndim)

# Give an array any dimension
new = np.array(17)
print(new)
print("Dimension of new: ", new.ndim)
new_2 = np.array([[17, 129], [21, 41]], ndmin=5)
print(new_2)
print("Dimension of new: ", new_2.ndim)
