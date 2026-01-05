import numpy as np

def count_spanning_trees(rows, cols):
    """
    Computes the number of spanning trees for a grid graph of size rows x cols vertices
    using the Matrix Tree Theorem.
    """
    n_vars = rows * cols
    laplacian = np.zeros((n_vars, n_vars))

    for r in range(rows):
        for c in range(cols):
            idx = r * cols + c
            # Find all neighbors in the grid
            neighbors = []
            if r > 0: neighbors.append((r - 1) * cols + c)
            if r < rows - 1: neighbors.append((r + 1) * cols + c)
            if c > 0: neighbors.append(r * cols + (c - 1))
            if c < cols - 1: neighbors.append(r * cols + (c + 1))

            # Laplacian matrix definition: L_ii = degree, L_ij = -1 if edge exists
            laplacian[idx, idx] = len(neighbors)
            for neighbor in neighbors:
                laplacian[idx, neighbor] = -1

    # The number of spanning trees is the determinant of any cofactor of the Laplacian
    reduced_laplacian = laplacian[1:, 1:]
    return int(round(np.linalg.det(reduced_laplacian)))

def solve():
    # A six-by-one checkerboard (6x1 squares) corresponds to a grid of 2x7 vertices.
    res1 = count_spanning_trees(2, 7)
    print(f"res1 = {res1}")

    # A two-by-two checkerboard (2x2 squares) corresponds to a grid of 3x3 vertices.
    res2 = count_spanning_trees(3, 3)
    print(f"res2 = {res2}")

    # The final answer is the product of the two results.
    return res1 * res2

print(solve())
