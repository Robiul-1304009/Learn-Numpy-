# Basic of operations on Arrays
import numpy as np

# Create Array of between number using 'a_range'
a = np.arange(0, 5)   # 1 dimensional array from 0 to 4
print("a:\n", a)
# Basic Mathematical operations on arrays
b = np.array([4, 6, 19, 23, 45])  # 1 dimensional array of 5 elements
print("b:\n", b)
# Adding
print("Adding a+b:\n", a+b)  # 1 dimension array of added value of a and b
# Subtracting
print("Subtracting b-a:\n", b-a)
# Multiplying
print("Multiplying a by 3:\n", a*3)
# Square all elements of a
print("Square(a):\n", a**2)
print("Built in Square(a):\n", np.square(a))
# Square rooting
print("Square root(a):\n", np.sqrt(a))
# Testing whether values in an array are less than a given value
c = np.array([1, 2, 3, 4])
print("Values in c array is less than 2:\n", c < 2)
print("Values in c array is less than 5:\n", c < 5)
