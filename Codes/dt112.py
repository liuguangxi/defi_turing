import numpy as np

# Define the coefficients matrix A for the 10 linear equations
# Grid variables: row 1 (x0, x1, x2, x3, x4), row 2 (x5, x6, x7, x8, x9)
A = np.zeros((10, 10))
B = np.zeros(10)

# Neighbor constants from the grid:
# Top: [4, 7, 1, 2, 1], Bottom: [10, 2, 7, 1, 0]
# Left: [10, 0], Right: [0, 1]

# Row 1 equations: 4*x[i] = neighbors_sum
A[0, 0], A[0, 1], A[0, 5], B[0] = 4, -1, -1, 4 + 10
A[1, 1], A[1, 0], A[1, 2], A[1, 6], B[1] = 4, -1, -1, -1, 7
A[2, 2], A[2, 1], A[2, 3], A[2, 7], B[2] = 4, -1, -1, -1, 1
A[3, 3], A[3, 2], A[3, 4], A[3, 8], B[3] = 4, -1, -1, -1, 2
A[4, 4], A[4, 3], A[4, 9], B[4] = 4, -1, -1, 1 + 0

# Row 2 equations
A[5, 5], A[5, 0], A[5, 6], B[5] = 4, -1, -1, 10 + 0
A[6, 6], A[6, 5], A[6, 1], A[6, 7], B[6] = 4, -1, -1, -1, 2
A[7, 7], A[7, 6], A[7, 2], A[7, 8], B[7] = 4, -1, -1, -1, 7
A[8, 8], A[8, 7], A[8, 3], A[8, 9], B[8] = 4, -1, -1, -1, 1
A[9, 9], A[9, 8], A[9, 4], B[9] = 4, -1, -1, 0 + 1

# Solve the linear system
x = np.linalg.solve(A, B)
print(x)

# Calculate the product of non-zero whole numbers
product = 1
for val in np.round(x):
    if val != 0:
        product *= int(val)

print(product)
