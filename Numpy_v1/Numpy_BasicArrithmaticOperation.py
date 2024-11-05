# Example 2: NumPy - Basic Arithmetic Operations
import numpy as np

# Creating arrays - 1D Array
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Arithmetic operations
addition= np.add(array1, array2)
subtraction = np.subtract(array2, array1)
multiplication = np.multiply(array1, array2)
division = np.divide(array1, array2)


# Printing
print('Added:', addition)
print('Subtracted:', subtraction)
print('Multiplied:', multiplication)
print('Divided:', division)