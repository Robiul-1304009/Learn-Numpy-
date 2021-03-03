# Copy and View in numpy

import numpy as np

# Copy
arr = np.array([1, 2, 3, 4, 5])  # One dimensional
print(arr)
copy = arr.copy()
print(copy)
# Change values in a array
arr[0] = 10
print(arr)  # print original = value changes
print(copy)  # print Copy  = value unchanged

# View
arr2 = np.array([6, 7, 8, 9, 10])
view = arr2.view()  # Creates a view of original array
print(view)
# Change values in a array
arr2[0] = 1
print(arr2)  # print original = value changes
print(view)  # print View  = value changes

# Change view
view[0] = 99
print(arr2)   # print original = value changes
print(view)   # print View  = value changes

# Python recall whether it's copy or view
print(view.base)  # Return a array with changes = [99, 7, 8, 9, 10]
print(copy.base)  # Returns = None
