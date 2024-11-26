# Install NumPy (Run in the terminal, not inside the script)
# pip install numpy

import numpy as np

# Creating arrays using lists
array_from_list = np.array([1, 2, 3, 4, 5])

# Creating arrays using built-in functions
zeros_array = np.zeros((3, 3))  # 3x3 array of zeros
ones_array = np.ones((2, 4))    # 2x4 array of ones
random_array = np.random.rand(4, 4)  # 4x4 array with random values

# Display arrays and their attributes
print("Array from list:", array_from_list)
print("Shape:", array_from_list.shape)
print("Data type:", array_from_list.dtype)

print("\nZeros Array:\n", zeros_array)
print("Shape:", zeros_array.shape)
print("Data type:", zeros_array.dtype)

print("\nOnes Array:\n", ones_array)
print("Shape:", ones_array.shape)
print("Data type:", ones_array.dtype)

print("\nRandom Array:\n", random_array)
print("Shape:", random_array.shape)
print("Data type:", random_array.dtype)
