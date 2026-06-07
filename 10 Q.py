import numpy as np

# Create 2D array
a = np.array([[1, 2, 3],
              [4, 5, 6]])

# Print shape
print("Shape:", a.shape)

# Print size
print("Size:", a.size)

# Print itemsize
print("Item Size:", a.itemsize)

# Print dtype
print("Datatype:", a.dtype)

# Change datatype
b = a.astype(float)

print("Changed Datatype:", b.dtype)

#Print ndim
print(a.ndim)
