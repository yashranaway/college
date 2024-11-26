# Initialize a list with integers
arr = [1, 2, 3, 4, 5]
print(f"Initial array: {arr}")

# 1. Insertion
# Insert an element at the beginning
arr = [0] + arr  # Equivalent to arr.insert(0, 0)
print(f"After inserting 0 at the beginning: {arr}")

# Insert an element at the end
arr += [6]  # Equivalent to arr.append(6)
print(f"After appending 6 at the end: {arr}")

# Insert an element at a specific index
arr = arr[:3] + [10] + arr[3:]  # Insert 10 at index 3
print(f"After inserting 10 at index 3: {arr}")

# 2. Deletion
# Remove an element by value
arr = [x for x in arr if x != 10]  # Remove all occurrences of 10
print(f"After removing 10: {arr}")

# Remove the last element
arr = arr[:-1]  # Equivalent to arr.pop()
print(f"After popping the last element: {arr}")

# Remove an element at a specific index
arr = arr[:1] + arr[2:]  # Remove the element at index 1
print(f"After deleting element at index 1: {arr}")

# 3. Searching
# Search for an element in the list
search_element = 3
if search_element in arr:
    print(f"Element {search_element} found in the array.")
else:
    print(f"Element {search_element} not found in the array.")

# 4. Iteration
# Iterate through the elements of the list
print("Iterating through the array:")
for element in arr:
    print(element)