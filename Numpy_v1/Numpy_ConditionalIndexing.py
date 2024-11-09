# Example 8: NumPy - Conditional Indexing
import numpy as np

# Creating an Array
array = np.array([1, 2, 3, 4, 5, 6, 7])

# Setting elements that satisfy a condition
array[array % 2 == 0] = -1              # Set even numbers to -1 (it will replace by -1 when found even number)

# Prining
print('Array after Conditional Indexing:', array)