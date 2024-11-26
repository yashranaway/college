import numpy as np

# Create two arrays
array1 = np.array([10, 20, 30, 40])
array2 = np.array([1, 2, 3, 4])

# Perform element-wise operations
add_result = array1 + array2
sub_result = array1 - array2
mul_result = array1 * array2
div_result = array1 / array2

# Using universal functions
sqrt_result = np.sqrt(array1)
log_result = np.log(array1)
exp_result = np.exp(array1)

print("Element-wise Addition:", add_result)
print("Element-wise Subtraction:", sub_result)
print("Element-wise Multiplication:", mul_result)
print("Element-wise Division:", div_result)

print("\nSquare Root of Array1:", sqrt_result)
print("Logarithm of Array1:", log_result)
print("Exponential of Array1:", exp_result)

