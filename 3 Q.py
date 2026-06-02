import numpy as np

# Create array from 1 to 12
a = np.arange(1, 13)

# Reshape into different shapes
b = a.reshape(3, 4)
c = a.reshape(2, 6)
d = a.reshape(2, 3, 2)

# Print outputs
print("Original Array:")
print(a)

print("\nShape (3,4):")
print(b)

print("\nShape (2,6):")
print(c)

print("\nShape (2,3,2):")
print(d)