import numpy as np

a = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

# First row
print("First row:", a[0])

# Second column
print("Second column:", a[:,1])

# Element 50
print("Element 50:", a[1,1])