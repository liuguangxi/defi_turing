import math

def find_largest_tri_tetra():
    # Triangular numbers: T_n = n(n+1)/2
    # Tetrahedral numbers: Te_m = m(m+1)(m+2)/6
    # This problem reduces to solving n(n+1)/2 = m(m+1)(m+2)/6.
    # It is mathematically proven (Stroeker, 1995) that the only
    # solutions are 1, 10, 120, 1540, and 7140.

    largest = 0
    # Search in a range to find the known solutions
    for m in range(1, 2000):
        tetra = m * (m + 1) * (m + 2) // 6
        # A number x is triangular if 8x + 1 is a perfect square
        test = 8 * tetra + 1
        root = math.isqrt(test)
        if root * root == test:
            largest = tetra

    return largest

print(find_largest_tri_tetra())
