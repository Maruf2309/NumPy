
# Example 30: NumPy - Combining Multiple Indexing Techniques
import numpy as np

# Creating a 2D array
array = np.array([[10, 20, 30], [40, 50, 60], [70,80,90]])

# Combining boolean, fancy, and slice indexing
#result = array[array > 30][:, [0, 2]]

# print('Combined Indexing Result:', result)


# Creating a boolean mask
mask = array > 30

# Applying the mask and reshaping to the original array shape (for demonstration)
filtered_array = np.where(mask, array, np.nan)  # Using np.nan to keep the shape

# Selecting the intended elements (fancy indexing)
result = filtered_array[:, [0, 2]]

print('Combined Indexing Result:')
print(result)






