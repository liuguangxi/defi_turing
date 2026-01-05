def solve():
    """
    Computes H(n), the number of regular hexagons in a triangular grid of side n.

    A regular hexagon is determined by its center point and a vector to one vertex.
    In the coordinate system (x, y, z) where x + y + z = n and x, y, z >= 0,
    a regular hexagon with vertices as grid points must have an integer center.
    The 6 vertices are defined by 6 vectors derived from a pair (a, b) such that
    the "spread" in each coordinate direction is s = a + b.

    For a fixed s, the number of possible positions for the center is the
    (n - 3s + 1)-th triangular number, T(n - 3s).
    The number of distinct regular hexagon orientations for a fixed s is s.
    Thus, H(n) = sum_{s=1 to floor(n/3)} s * (n - 3s + 1) * (n - 3s + 2) / 2.
    """
    limit = 1000

    def H(n):
        total = 0
        # The hexagon must fit within the triangle of side n.
        # This requires the spread in each direction to be 2s,
        # leading to the center constraint s <= x_c <= n-s.
        for s in range(1, n // 3 + 1):
            # Number of integer solutions to x' + y' + z' = n - 3s
            # is (n - 3s + 1) * (n - 3s + 2) // 2.
            num_positions = (n - 3 * s + 1) * (n - 3 * s + 2) // 2
            total += s * num_positions
        return total

    # Summing H(n) for n from 3 to 1,000.
    result = sum(H(n) for n in range(3, limit + 1))
    return result

print(solve())
