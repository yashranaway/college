import numpy as np

# Create an array
array = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]])

# Indexing specific elements
element = array[1, 2]  # Element in second row, third column

# Accessing specific rows and columns
row = array[1, :]  # Second row
column = array[:, 2]  # Third column

# Slicing to extract subarrays
subarray = array[0:2, 1:3]  # Slice a 2x2 subarray

# Boolean indexing
bool_index = array[array > 50]

# Fancy indexing
fancy_index = array[[0, 2], [1, 3]]  # Selecting elements (0,1) and (2,3)

print("Original Array:\n", array)
print("\nSpecific Element [1, 2]:", element)
print("\nSpecific Row (1):", row)
print("\nSpecific Column (2):", column)
print("\nSubarray (0:2, 1:3):\n", subarray)
print("\nBoolean Indexing (elements > 50):", bool_index)
print("\nFancy Indexing ([0,2], [1,3]):", fancy_index)

