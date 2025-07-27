import random

# Generate two random lists of 10 unique numbers each
list1 = random.sample(range(1, 100), 10)
list2 = random.sample(range(1, 100), 10)

# Find common elements between the two lists (no duplicates)
common_elements = set(list1) & set(list2)

# Display the results
print("List 1:", list1)
print("List 2:", list2)
print("Common elements:", list(common_elements))
