# Shape and Reshape Arrays
import numpy as np

# Shape of an array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Array:\n", arr)
print("Shape:\n", arr.shape)

# Reshaping array
student = np.array([19, 19, 19, 20, 20, 20, 20, 21, 21, 21])
exam_score = np.array([57, 60, 65, 59, 63, 70, 75, 75, 75])
# Splitting
exan_split = exam_score.reshape(3, 3)
exan_split2 = exam_score.reshape(9, 1)
exan_split3 = exam_score.reshape(3, 3, 1)
print("Exam Score in 1 dimension:\n", exam_score)
print("Splitted in 2 dimension of 3 arrays:\n", exan_split)
print("Splitted in 2 dimension of 9 arrays:\n", exan_split2)
print("Splitted in 3 dimension of 3 arrays of 2 dimension "
      "and 9 arrays in 1 dimension :\n", exan_split3)

