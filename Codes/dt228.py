def solve_hyperball_integer_points():
    """
    Computes T(r), the number of integer points (x, y, z, t) such that
    x^2 + y^2 + z^2 + t^2 <= r^2.

    This is equivalent to the sum of r_4(n) for n from 0 to floor(r^2),
    where r_4(n) is the number of ways to write n as the sum of four squares.
    Jacobi's four-square theorem states that for n > 0:
    r_4(n) = 8 * sum_{d|n, 4 does not divide d} d.

    Therefore, T(r) = r_4(0) + sum_{n=1 to r^2} 8 * sum_{d|n, 4 !| d} d.
    Using the identity for the sum of the divisor function:
    sum_{n=1 to N} sum_{d|n} d = sum_{d=1 to N} d * floor(N/d).

    T(r) = 1 + 8 * sum_{d=1 to r^2, 4 !| d} d * floor(r^2 / d).
    """
    r = 500
    r_sq = r * r

    # Calculate the sum using the divisor sum identity
    # Time complexity: O(r^2), which is O(250,000) for r=500.
    total_points = 1
    for d in range(1, r_sq + 1):
        if d % 4 != 0:
            total_points += 8 * d * (r_sq // d)

    return total_points

print(solve_hyperball_integer_points())
