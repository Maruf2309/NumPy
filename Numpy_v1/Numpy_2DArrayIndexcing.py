# Example 2: NumPy - 2D Array Indexing
import numpy as np
# creating a 2D array
array_2d = np.array([[1, 2, 3],[4,5,6], [7,8,9]])

# Accessing individual elements
element  = array_2d[1, 2]  # Accessing element at row 1, column 2   (1 mean 2nd row [4,5,6] and col 2 mean last val e.g 6)

# Slicing rows & columns
row_slice = array_2d[0, :] # first row & all cols
column_slice = array_2d[:, 1] # Second column        (all rows at 2nd cols)

# Prining
print('2D Array :', array_2d)
print('Element at (1,2):', element)
print('First Row : ', row_slice)
print('Second Column :', column_slice)