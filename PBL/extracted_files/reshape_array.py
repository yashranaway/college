import numpy as np

# Create a 1D array
array_1d = np.arange(1, 13)

# Reshape into different dimensions
array_2d = array_1d.reshape(3, 4)
array_3d = array_1d.reshape(2, 2, 3)

# Transpose the reshaped array
transposed_array = np.transpose(array_2d)

# Swap axes of the 3D array
swapped_axes_array = np.swapaxes(array_3d, 0, 2)

print("Original 1D Array:\n", array_1d)
print("\nReshaped to 2D (3x4):\n", array_2d)
print("\nReshaped to 3D (2x2x3):\n", array_3d)
print("\nTransposed 2D Array:\n", transposed_array)
print("\nSwapped Axes in 3D Array:\n", swapped_axes_array)

