# Example 19: NumPy - Clipping Array Values
import numpy as np

# Create an array
array = np.array([1, 2, 3, 4, 5]) # 1D

# Clipping values to be between 2 and 4
clippled_array = np.clip(array, 2, 4)   # Value 1 & 5 outside of the range, value below 2 all map to 2 and value > 4 all mapped down to 4

print('Original Array:', array)
print('Clipped Array:', clippled_array)

'''

### Notes
explain np.clip() function
The np.clip() function in NumPy is used to limit the values in an array. It ensures that all elements in the array fall within a specified range. 
Elements below the minimum value are set to the minimum, and elements above the maximum value are set to the maximum.

'''

# Creating an array
array2 = np.array([1, 4, 8, 12, 15]) 
# Applying np.clip
clipped_array2 = np.clip(array2, 3, 10)

print("Original Array-2:", array2) 
print("Clipped Array-2:", clipped_array2)