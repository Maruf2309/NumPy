# Example 7: NumPy - Indexing with Arrays
import numpy as np

# Creating a 2D array
array = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# Using arrays for indexing
rows = np.array([0, 1, 2])
cols = np.array([2, 1, 0])

indexed_elements = array[rows, cols]

print('Indexed Elements:', indexed_elements)